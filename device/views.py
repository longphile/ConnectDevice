from django.shortcuts import render
from .models import Device
from .forms import DeviceForm ,DevideInfoForm
from .serializers import DeviceSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
def index(request):
    devices = Device.objects.all()
    if request.method == 'POST':
        #print(request.POST)
        form = DeviceForm(request.POST)
        if form.is_valid() and "Add_Device" in request.POST:
            thingName = str(form['name'].value())
            thingType = str(form['type'].value())
            device = Device()
            device.name = thingName
            device.type = thingType
            if device.type == "Air Condition" :
                device.parameter = "temperature"
            else:
                device.parameter = "level"
            device.currentMode = "Auto"
            device.desireMode = "Auto"
            device.value = "0"
            device.threshold_up = "0"
            device.threshold_down = "0"
            device.currentState = "Off"
            device.desireState = "Off"
            device.connect = "disconnect"
            device.save()
        else: 
            form = DevideInfoForm(request.POST)
            mode = ''
            state = ''
            if form.is_valid():
                mode = form['mode'].value()
                state = form['state'].value()
                #print(form['mode'].value())
                #print(form['state'].value())
            for device in devices:
                #print(device.name)
                if device.name in request.POST:# and device.connect == "connect":
                    print(device.name)
                    if mode != device.desireMode :
                        device.desireMode = mode
                    if(mode == "Manual" and state != device.desireState) :
                        device.desireState = state
                    device.save()
    form = DeviceForm()

    
    deviceid_data = []
    # DevideInfo_FormSet=DevideInfoForm()
    devices = Device.objects.all()
    for item in devices:
        DeviceInfo = DevideInfoForm() 
        device = {
            'name' : item.name,
            'type' : item.type,
            'connect' : item.connect,
            'parameter' : item.parameter,
            'value' : item.value,
            'mode' : item.currentMode,
            'state':item.currentState,
            'DeviceInfo':DeviceInfo
        }
        # print(item)
        deviceid_data.append(device)
    # print(deviceid_data)
    context = {'deviceid_data' : deviceid_data, 'form' : form }

    return render(request, 'device.html', context)

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_device(request, pk):
#    try:
#        employee = Employee.objects.get(pk=pk)
#    except Employee.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single employee
    if request.method == 'GET':
        return Response({})
    # delete a single employee
    elif request.method == 'DELETE':
        return Response({})
    # update details of a single employee
    elif request.method == 'PUT':
        return Response({})
        
@api_view(['GET', 'POST'])
def get_post_device(request):
    # get all employee
    if request.method == 'GET':
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)
        #return Response({})
    # insert a new record for a employee
    elif request.method == 'POST':
        if "name" in request.data and ("threshold_up" in request.data or "threshold_down" in request.data or  "parameter"  in request.data or "value" in request.data 
        or "currentState" in request.data or "desireState" in request.data
        or "currentMode" in request.data or "desireMode" in request.data) :
            device = Device.objects.get(name=request.data.get('name'))
            if "currentMode" in request.data and device.currentMode != request.data.get('currentMode'):
                device.currentMode = request.data.get('currentState')
            if "desireMode" in request.data and device.desireMode != request.data.get('desireMode'):
                device.desireMode = request.data.get('desireState')
            if "threshold_up" in request.data :
                device.threshold_up = request.data.get('threshold_up')
            if "threshold_down" in request.data :
                device.threshold_up = request.data.get('threshold_down')
            if "parameter"  in request.data :
                device.parameter = request.data.get('parameter')            
            if "value" in request.data:                
                device.value = request.data.get('value')
                if float(device.value) > float(device.threshold_up) and device.currentMode == "Auto":
                    device.desireState = "On"
                if float(device.value) < float(device.threshold_down) and device.currentMode == "Auto":
                    device.desireState = "Off"                        
            if "currentState" in request.data and device.currentState != request.data.get('currentState'):
                device.currentState = request.data.get('currentState')
            if "desireState" in request.data and device.threshold_up != request.data.get('desireState'):
                device.desireState = request.data.get('desireState')
            device.save()
            serializer = DeviceSerializer(device)
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            if "name" in request.data:
                serializer = DeviceSerializer(Device.objects.get(name=request.data.get('name')))
                return Response(serializer.data,status=status.HTTP_200_OK)
            elif "type" in request.data:
                serializer = DeviceSerializer(Device.objects.get(name=request.data.get('type')))
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)