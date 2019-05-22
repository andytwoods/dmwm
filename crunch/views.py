import csv
import re

import unicodecsv as unicodecsv
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from csv import reader

from django.utils.datetime_safe import datetime
from django.utils.decorators import method_decorator

from crunch.forms import CrunchForm

# Create your views here.
from django.views.generic import FormView

from crunch.models import ZohoInfo


@method_decorator(login_required, name='dispatch')
class Crunch(FormView):
    template_name = 'crunch/crunch.html'
    form_class = CrunchForm
    success_url = reverse_lazy('crunch')

    def split_line(self, str):
        csv_list = ['"{}"'.format(x) for x in list(csv.reader([str], delimiter=','))[0]]
        return [x.replace('"', '') for x in csv_list]

    def form_valid(self, form):

        data = form.data['data']

        headers = None

        infos = []
        skip = 1

        current_year = datetime.now().year

        for r in data.split('\n'):
            r = r.replace('\r', '')

            if skip > 0:
                skip -= 1
                continue
            elif headers is None:
                headers = self.split_line(r)

            else:
                position_locked_vals = self.split_line(r)

                position_locked_vals_len = len(position_locked_vals)
                if position_locked_vals_len == 0:
                    continue
                if position_locked_vals_len != len(headers):
                    raise Exception(f'csv formatting issue (header count {len(headers)} and data count '
                                    f'{position_locked_vals_len} not the same) so stopping here: ' + r)

                params = {key.replace(' ', '_').replace('\"', ''): val for key, val, in
                          zip(headers, position_locked_vals)}

                info = ZohoInfo()

                info.Company = params.get('Company_Name', None)
                info.No_of_Employees = params.get('Employees', None)

                # info.Company = params.get('SIC_2007_Description', None)
                # info.Company = params.get('Trading_Address', None)
                info.Trading_Address = params.get('Trading_Address_1', None)
                info.Trading_Town_City = params.get('Trading_Address_2', None)
                info.Province = params.get('Trading_Address_3', None)
                # info.Trading_Address = params.get('Trading_Address_4', None)
                info.Trading_Post_Code = params.get('Trading_Address_Postcode', None)
                # info.Company = params.get('Trading_Post_Town', None)
                info.Website = params.get('Web_Address_1', None)
                info.Year_Company_Was_Founded = current_year - int(params.get('Age', 0))

                infos.append(info)

        if len(infos) > 0:
            ZohoInfo.objects.bulk_create(infos)

        messages.success(self.request, f'added records {len(infos)} to your database')

        return super().form_valid(form)


@staff_member_required
def export(request):
    data = list(ZohoInfo.objects.all())
    headers = [f.name for f in ZohoInfo._meta.get_fields()]
    try:
        headers.remove('Ready_To_Zoho')
    except ValueError:
        pass
    try:
        headers.remove('Uploaded_To_Zoho')
    except ValueError:
        pass
    try:
        headers.remove('id')
    except ValueError:
        pass

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=expt_%s.csv' % datetime.strftime(
        datetime.now(), '%Y%m%d%H%M%S%f')

    writer = unicodecsv.writer(response, encoding='utf', dialect='excel')

    zoho_headers = []
    for header in headers:
        if '_' in header:
            header.replace('_', ' ')
            header = '"' + header + '"'
        zoho_headers.append(header)

    writer.writerow(zoho_headers)

    for info in data:
        row = []
        for header in headers:
            found = getattr(info, header, None)
            row.append(found)
        writer.writerow(row)

    return response
