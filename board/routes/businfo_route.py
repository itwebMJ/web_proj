from flask import Blueprint, render_template, request, redirect, session
import board.models.businfo as bus

bp = Blueprint('businfo', __name__, url_prefix='/businfo')
bus_service = bus.BusService()


@bp.route('/')
def root():
    return render_template('businfo/location.html')

@bp.route('/getroute-list', methods=['POST'])
def route_list():
    loc = request.form['loc']
    list = bus_service.getBusRouteList(loc)
    return render_template('businfo/route_list.html', list=list)

@bp.route('/getroute-info')
def getroute_info():
    routeId = request.args.get('routeId', '', str)
    bus = bus_service.getRouteInfoItem(routeId)
    stations = bus_service.getStaionsByRouteList(routeId)
    return render_template('businfo/detail.html', bus=bus, stations=stations)




