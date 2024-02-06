from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import leave_request_form
# from django.http import HttpResponse

# #leave

# #from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
# from .models import LeaveRequest
# # Create your views here.


# def loginsystem(request):
#     return HttpResponse('SNS Portal')



# @login_required
# def leave_request(request):
#     if request.method == 'POST':
#         data = request.POST
#         employee = request.user.id
#         start_date = data.get('start_date')
#         end_date = data.get('end_date')
#         leave_type = data.get('leave_type')
#         reason = data.get('reason')

#         leave_request = LeaveRequest.objects.create(
#             employee=employee,
#             start_date=start_date,
#             end_date=end_date,
#             leave_type=leave_type,
#             reason=reason,
#         )

#         return HttpResponse({'message': 'Leave request submitted successfully', 'id': leave_request.id})

# @login_required
# def leave_approve(request, id):
#     leave_request = LeaveRequest.objects.get(id=id)
#     leave_request.status = 'Approved'
#     leave_request.message = 'Your leave request has been approved.'
#     leave_request.save()

#     return HttpResponse({'message': 'Leave request approved successfully'})

# @login_required
# def leave_reject(request, id):
#     leave_request = LeaveRequest.objects.get(id=id)
#     leave_request.status = 'Rejected'
#     leave_request.message = 'Your leave request has been rejected.'
#     leave_request.save()

#     return HttpResponse({'message': 'Leave request rejected successfully'})


def firstpage(request):
    return render(request,"firstpage.html")

def login(request):
     return render(request,"login.html")



def leave_request_form(request):
    if request.method == 'POST':
        form = leave_request_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = leave_request_form()

    return render(request, 'loginsystem/leave_request_form.html', {'form': form})

def success(request):
    return render(request, 'loginsystem/success.html')