#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    ver 0.01
    2025/04/18
    2025/04/18
"""
__author__ = 'oxxpeh'

import datetime as ii_dt
import json as ii_js
import plotly as ii_pl
import pyscript as ii_pys
import requests as ii_rq
import time as ii_tm

from js import document as ij_dc
from js import window as ij_wd


def ff_get_ym() -> str:
    """
    指定されたURLから情報を取得します。

    Returns:
        str: 図情報のテキスト
    """
    #if rt.ok:
    #   text = await rt.text()
    #   ij_wd.console.log(text)  # コンソールに出力
    
    rt = ii_rq.get('https://oxxpeh.github.io/2025/fig.json')

    #df_tck = ii_pc.loads(rt.content)
    ij_wd.console.log(f"@ -- rt {rt} ")
    aas_txt = rt.text
    ij_wd.console.log(f"@ -- text {aas_txt} ")
    #dd_ym = ii_js.loads(aas_txt)
    #return(dd_ym)
    return(aas_txt)

def ff_draw_plot() -> None:
    """プロットを描画します。

    初期データを使用してPlotlyで散布図を作成します。
    """
    x_data = [1, 2, 3, 4]
    y_data = [10, 15, 13, 17]
    dd_data = [{
        'x': x_data,
        'y': y_data,
        'type': 'scatter',
        'mode': 'lines+markers',
        'name': 'Initial Data'
    }]
    dd_layout = {
        'title': 'Initial Plot',
        'xaxis': {'title': 'X Axis'},
        'yaxis': {'title': 'Y Axis'}
    }
    js_data = ii_js.dumps(dd_data)
    js_layout = ii_js.dumps(dd_layout)
    ij_wd.Plotly.newPlot('ele_plot', ij_wd.JSON.parse(js_data), ij_wd.JSON.parse(js_layout))

def ff_main() -> None:
    """メイン処理を実行します。

    データを取得し、Plotlyを使用してプロットを作成します。
    """
    aas_txt = ff_get_ym()
    #ij_wd.console.log(f"@ -- dd_ym {dd_ym} ")
    ij_wd.Plotly.newPlot('ele_plot', ij_wd.JSON.parse(aas_txt))

dt_nw = ii_dt.datetime.now()
ij_wd.console.log(f"@ -- start {dt_nw} ")
#ff_draw_plot()
ff_main()
ij_wd.console.log(f"@ -- end")