import csv
import re

from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from csv import reader

from crunch.forms import CrunchForm

# Create your views here.
from django.views.generic import FormView

from crunch.models import Info


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

                params = {key.replace(' ', '_').replace('\"', ''): val for key, val, in zip(headers, position_locked_vals)}
                print(params)
                info = Info(**params)

                infos.append(info)
                print(info.Company_Name)

        if len(infos) > 0:
            Info.objects.bulk_create(infos)

        messages.success(self.request, f'added records {len(infos)} to your database')

        return super().form_valid(form)
