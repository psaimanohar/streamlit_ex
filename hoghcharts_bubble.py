import streamlit as st              
import streamlit_highcharts as hg              

chartDef={ 'labels': { 'items': [ { 'html': 'Total '
                                   'liter',
                           'style': { 'color': 'black',
                                      'left': '50px',
                                      'top': '18px'}}]},
  'series': [ { 'data': [ 59,
                          83,
                          65,
                          228,
                          184],
                'name': '2020',
                'type': 'column'},
              { 'data': [ 24,
                          79,
                          72,
                          240,
                          167],
                'name': '2021',
                'type': 'column'},
              { 'data': [ 58,
                          88,
                          75,
                          250,
                          176],
                'name': '2022',
                'type': 'column'},
              { 'data': [ 47,
                          83.33,
                          70.66,
                          239.33,
                          175.66],
                'marker': { 'fillColor': 'black',
                            'lineWidth': 2},
                'name': 'Average',
                'type': 'spline'},
              { 'center': [80, 70],
                'data': [ { 'color': '#7cb4ec',
                            'name': '2020',
                            'y': 619},
                          { 'color': '#434348',
                            'name': '2021',
                            'y': 586},
                          { 'color': '#90ed7d',
                            'name': '2022',
                            'y': 647}],
                'dataLabels': { 'enabled': False},
                'name': 'Liter',
                'showInLegend': False,
                'size': 100,
                'type': 'pie'}],
  'title': { 'align': 'left',
             'text': 'Sales of '
                     'petroleum '
                     'products March, '
                     'Norway'},
  'xAxis': { 'categories': [ 'Jet fuel',
                             'Duty-free '
                             'diesel',
                             'Petrol',
                             'Diesel',
                             'Gas '
                             'oil']},
  'yAxis': { 'title': { 'text': 'Million '
                                'liter'}}}


hg.streamlit_highcharts(chartDef,640)
