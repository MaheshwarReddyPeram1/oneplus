from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from onemoreapp.models import onetoone, weeklypresentation, dailypresentation, socials, visitors, referralsgiven, referralstaken, jvtthankyou, job, sphere, trainings, interview, invited, edittable
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import EmailMessage
from account.models import User


def home(request):
	user = User.objects.all()
	context = {
	'user' : user
	}
	return render(request,"home.html",context)

def adminpage(request):
	u = User.objects.all()
	context = { 'u' : u }
	if request.method == "POST":
		employeeid = request.POST['userid']
		request.session['user_id']=employeeid
		return redirect('viewreport/'+'user')
	return render(request,"adminpage.html",context)
def viewreport(request):
	userid=request.user.id
	o = onetoone.objects.filter(user_id=userid)
	d = dailypresentation.objects.filter(user_id=userid)
	w = weeklypresentation.objects.filter(user_id=userid)
	s = socials.objects.filter(user_id=userid)
	v = visitors.objects.filter(user_id=userid)
	g = referralsgiven.objects.filter(user_id=userid)
	y = jvtthankyou.objects.filter(user_id=userid)
	j = job.objects.filter(user_id=userid)
	s = sphere.objects.filter(user_id=userid)
	t = trainings.objects.filter(user_id=userid)
	m = interview.objects.filter(user_id=userid)
	i = invited.objects.filter(user_id=userid)
	context = {
	'o' : o,
	'd' : d,
	'w' : w,
	's' : s,
	'v' : v,
	'g' : g,
	't' : t,
	'j' : j,
	's' : s,
	't' : t,
	'm' : m,
	'i' : i,
	'y' : y
	}
	return render(request,"viewreport.html",context)
def viewreport1(request):
	userid=request.session.get('user_id')
	o = onetoone.objects.filter(user_id=userid)
	d = dailypresentation.objects.filter(user_id=userid)
	w = weeklypresentation.objects.filter(user_id=userid)
	s = socials.objects.filter(user_id=userid)
	v = visitors.objects.filter(user_id=userid)
	g = referralsgiven.objects.filter(user_id=userid)
	y = jvtthankyou.objects.filter(user_id=userid)
	j = job.objects.filter(user_id=userid)
	s = sphere.objects.filter(user_id=userid)
	t = trainings.objects.filter(user_id=userid)
	m = interview.objects.filter(user_id=userid)
	i = invited.objects.filter(user_id=userid)
	# print(userid)
	context = {
	'o' : o,
	'd' : d,
	'w' : w,
	's' : s,
	'v' : v,
	'g' : g,
	't' : t,
	'j' : j,
	's' : s,
	't' : t,
	'm' : m,
	'i' : i,
	'y' : y
	}
	return render(request,"viewreport.html",context)

# def viewreport(request):
# 	o = onetoone.objects.raw(f'select onetooneid from onemoreapp_onetoone where user_id = {request.user.id}')
# 	d = dailypresentation.objects.raw(f'select dailypresentationid from onemoreapp_dailypresentation where user_id = {request.user.id}')
# 	w = weeklypresentation.objects.raw(f'select weeklypresentationid from onemoreapp_weeklypresentation where user_id = {request.user.id}')
# 	s = socials.objects.raw(f'select socialsid from onemoreapp_socials where user_id = {request.user.id}')
# 	v = visitors.objects.raw(f'select visitorsid from onemoreapp_visitors where user_id = {request.user.id}')
# 	g = referralsgiven.objects.raw(f'select referralsgivenid  from onemoreapp_referralsgiven where user_id = {request.user.id}')
# 	y = jvtthankyou.objects.raw(f'select jvtthankyouid from onemoreapp_jvtthankyou where user_id = {request.user.id}')
# 	j = job.objects.raw(f'select jobid from onemoreapp_job where user_id = {request.user.id}')
# 	s = sphere.objects.raw(f'select sphereid from onemoreapp_sphere where user_id = {request.user.id}')
# 	t = trainings.objects.raw(f'select trainingid from onemoreapp_trainings where user_id = {request.user.id}')
# 	m = interview.objects.raw(f'select interviewid from onemoreapp_interview where user_id = {request.user.id}')
# 	i = invited.objects.raw(f'select invitedid from onemoreapp_invited where user_id = {request.user.id}')
# 	context = {
# 	'o' : o,
# 	'd' : d,
# 	'w' : w,
# 	's' : s,
# 	'v' : v,
# 	'g' : g,
# 	't' : t,
# 	'j' : j,
# 	's' : s,
# 	't' : t,
# 	'm' : m,
# 	'i' : i,
# 	'y' : y
# 	}
# 	return render(request,"viewreport.html",context)

def one2one(request):
	if request.method == "POST":
		userid=request.user.id
		one2one = onetoone()
		one2one.user_id=userid
		one2one.onemet = request.POST['met']
		one2one.oneinvited = request.POST['invited']
		one2one.oneratings = request.POST['ratings']
		one2one.onetopic = request.POST['topic']
		one2one.onedate = request.POST['Date']
		one2one.save()
		return HttpResponseRedirect('home')


def weeklypre(request):
	if request.method == "POST":
		userid=request.user.id
		week = weeklypresentation()
		week.user_id = userid
		week.weektopic= request.POST['topic']
		week.weekduration= request.POST['time']
		week.weekdate= request.POST['Date']
		week.weekbestby = request.POST['bestby']
		week.save()
		return HttpResponseRedirect('home')

def dailypre(request):
	if request.method == "POST":
		daily = dailypresentation()
		userid=request.user.id
		daily.user_id= userid
		daily.dailytopic = request.POST['topic']
		daily.dailyduration = request.POST['time']
		daily.dailydate = request.POST['Date']
		daily.dailybestby = request.POST['bestby']
		daily.save()
		return HttpResponseRedirect('home')

def social(request):
	if request.method == "POST" and request.FILES:
		social_s = socials()
		userid=request.user.id
		social_s.user_id= userid
		social_s.socialstopic = request.POST['topic']
		social_s.socialsplace = request.POST['place']
		social_s.socialsdate = request.POST['Date']
		social_s.socialspic = request.FILES['pic']
		social_s.save()
		return HttpResponseRedirect('home')


def visitor(request):
	if request.method == "POST":
		visitor_s = visitors()
		# visitor_s.user = users.objects.raw(f'select user_id from onemoreapp_users where user_id = {request.user.id}')[0]
		userid=request.user.id
		visitor_s.user_id= userid
		visitor_s.visitorstopic = request.POST['topic']
		visitor_s.visitorsnumbers = request.POST['visnumber']
		visitor_s.visitorsdate = request.POST['Date']
		visitor_s.visitorspic = request.FILES['pic']
		visitor_s.save()
		return HttpResponseRedirect('home')


def given(request):
	if request.method == "POST":
		ref = referralsgiven()
		# ref.user = users.objects.raw(f'select user_id from onemoreapp_users where user_id = {request.user.id}')[0]
		userid=request.user.id
		ref.user_id= userid
		ref.givenby = request.POST['refgivenby']
		ref.giventype = request.POST['reftype']
		ref.givenaddress = request.POST['address']
		ref.givenphonenumber = request.POST['phonenumber']
		ref.save()
		return HttpResponseRedirect('home')


def thankyou(request):
	if request.method == "POST":
		thank = jvtthankyou()
		# thank.user = users.objects.raw(f'select user_id from onemoreapp_users where user_id = {request.user.id}')[0]
		userid=request.user.id
		thank.user_id= userid
		thank.youto = request.POST['name']
		thank.youamount = request.POST['amount']
		thank.youbtype = request.POST['businesstype']
		thank.yourtype = request.POST['refname']
		thank.save()
		return HttpResponseRedirect('home')


def jobrecommendation(request):
	if request.method == "POST":
		rec = job()
		# rec.user = users.objects.raw(f'select user_id from onemoreapp_users where user_id = {request.user.id}')[0]
		userid=request.user.id
		rec.user_id= userid
		rec.recname = request.POST['name']
		rec.recexp = request.POST['experience']
		rec.recctc = request.POST['ctc']
		rec.recdate = request.POST['Date']
		rec.reccomname = request.POST['companyname']
		rec.save()
		return HttpResponseRedirect('home')

def contactsphere(request):
	if request.method == "POST":
		contact = sphere()
		# contact.user = users.objects.raw(f'select user_id from onemoreapp_users where user_id = {request.user.id}')[0]
		userid=request.user.id
		contact.user_id= userid
		contact.spherename = request.POST['name']
		contact.spherenumber = request.POST['number']
		contact.spheremail = request.POST['email']
		contact.save()
		return HttpResponseRedirect('home')

def training(request):
	if request.method == "POST":
		train = trainings()
		# train.user = users.objects.raw(f'select user_id from onemoreapp_users where user_id = {request.user.id}')[0]
		userid=request.user.id
		train.user_id= userid
		train.startdate = request.POST['startdate']
		train.enddate = request.POST['enddate']
		train.subject = request.POST['subject']
		train.rating = request.POST['rating']
		train.save()
		return HttpResponseRedirect('home')

def mockinterview(request):
	if request.method == "POST":
		mock = interview()
		# mock.user = users.objects.raw(f'select user_id from onemoreapp_users where user_id = {request.user.id}')[0]
		userid=request.user.id
		mock.user_id= userid
		mock.metwith = request.POST['metwith']
		mock.inviteby = request.POST['inviteby']
		mock.rating = request.POST['rating']
		mock.topic = request.POST['topic']
		mock.Date = request.POST['Date']
		mock.save()
		return HttpResponseRedirect('home')

def invite(request):
	if request.method == "POST":
		vis = invited()
		userid=request.user.id
		# vis.user = users.objects.raw(f'select user_id from onemoreapp_users where user_id = {request.user.id}')
		vis.user_id=userid
		vis.title = request.POST['title']
		vis.firstname = request.POST['firstname']
		vis.lastname = request.POST['lastname']
		vis.vcompanyname = request.POST['vcompanyname']
		vis.email = request.POST['email']
		vis.companyname = request.POST['companyname']
		vis.save()
		return HttpResponseRedirect('home')

def taken(request):
	if request.method == "POST":
		take = referralstaken()
		# take.user = users.objects.raw(f'select user_id from onemoreapp_users where user_id = {request.user.id}')[0]
		userid=request.user.id
		take.user_id= userid
		take.takentopic = request.POST['Topicname']
		take.takenduration = request.POST['firstname']
		take.takendate = request.POST['lastname']
		take.takendate = request.POST['vcompanyname']
		take.takendate = request.POST['email']
		take.takendate = request.POST['companyname']
		take.save()
		return HttpResponseRedirect('home')

# def onetooneview(request):
# 	admin_userid = request.session.get('employee_id_sess', None)
# 	o = onetoone.objects.raw(f'select onetooneid from onemoreapp_onetoone where user_id = {request.user.id}') or onetoone.objects.raw(f'select onetooneid from onemoreapp_onetoone where user_id = {admin_userid}')
# 	context = {'o' : o}
# 	return render(request,"onetooneview.html",context)

# def dailyview(request):
# 	admin_userid = request.session.get('employee_id_sess', None)
# 	d = dailypresentation.objects.raw(f'select dailypresentationid from onemoreapp_dailypresentation where user_id = {request.user.id}') or dailypresentation.objects.raw(f'select dailypresentationid from onemoreapp_dailypresentation where user_id = {admin_userid}')
# 	context = {'d' : d}
# 	return render(request,"dailyview.html",context)

# def weeklyview(request):
# 	admin_userid = request.session.get('employee_id_sess', None)
# 	w = weeklypresentation.objects.raw(f'select weeklypresentationid from onemoreapp_weeklypresentation where user_id = {request.user.id}') or weeklypresentation.objects.raw(f'select weeklypresentationid from onemoreapp_weeklypresentation where user_id = {admin_userid}')
# 	context = {'w' : w}
# 	return render(request,"weeklyview.html",context)

# def socialsview(request):
# 	admin_userid = request.session.get('employee_id_sess', None)
# 	s = socials.objects.raw(f'select socialsid from onemoreapp_socials where user_id = {request.user.id}') or socials.objects.raw(f'select socialsid from onemoreapp_socials where user_id = {admin_userid}')
# 	context = {'s' : s}
# 	return render(request,"socialsview.html",context)

# def visitorsview(request):
# 	admin_userid = request.session.get('employee_id_sess', None)
# 	v = visitors.objects.raw(f'select visitorsid from onemoreapp_visitors where user_id = {request.user.id}') or visitors.objects.raw(f'select visitorsid from onemoreapp_visitors where user_id = {admin_userid}')
# 	context = {'v' : v}
# 	return render(request,"visitorsview.html",context)

# def referralsgivenview(request):
# 	admin_userid = request.session.get('employee_id_sess', None)
# 	rg = referralsgiven.objects.raw(f'select referralsgivenid from onemoreapp_referralsgiven where user_id = {request.user.id}') or referralsgiven.objects.raw(f'select referralsgivenid from onemoreapp_referralsgiven where user_id = {admin_userid}')
# 	context = {'rg' : rg}
# 	return render(request,"referralsgivenview.html",context)

# def referralstakenview(request):
# 	admin_userid = request.session.get('employee_id_sess', None)
# 	rt = referralstaken.objects.raw(f'select referralstakenid from onemoreapp_referralstaken where user_id = {request.user.id}') or referralstaken.objects.raw(f'select referralstakenid from onemoreapp_referralstaken where user_id = {admin_userid}')
# 	context = {'rt' : rt}
# 	return render(request,"referralstakenview.html",context)

def profile(request):
	userid=request.user.id
	if edittable.objects.filter(user_id=userid).exists():
		profile = edittable.objects.filter(user_id=userid)
		# context = {'p' : p}
		print(profile[0].name)
		return render(request,"profile.html",{'p':profile[0]})
	return render(request,"profile.html")
def edit(request):
	if request.method == "POST":	
		user = edittable()
		# user.user = users.objects.raw(f'select user_id from onemoreapp_users where user_id = {request.user.id}')[0]
		userid=request.user.id
		print(userid)
		print('mahi23123')
		user.user_id=userid
		user.name = request.POST['username']
		user.email = request.POST['Email']
		user.phonenumber = request.POST['phonenumber']
		user.dob = request.POST['Date']
		user.gender = request.POST['gender']
		user.englishlevel = request.POST['englishlevel']
		user.Location = request.POST['Location']
		user.Address = request.POST['Address']
		user.Profession = request.POST['Profession']
		user.company = request.POST['company']
		user.joindate = request.POST['joindate']
		user.Experience = request.POST['Experience']
		user.skills = request.POST['skills']
		user.projects = request.POST['projects']
		user.course = request.POST['course']
		user.specialization = request.POST['specialization']
		user.year = request.POST['year']
		user.college = request.POST['college']
		user.resume = request.FILES['resume']
		user.image = request.FILES['image']
		user.save()
		return HttpResponseRedirect(reverse('profile'))
	else:
		print('mahi23123')
		return render(request,"edit.html")


def forgotpassword(request):
	if request.method == "POST":
		Email = request.POST['username']
		if User.objects.filter(email=Email).exists():
			# context = User.objects.raw(f"select user_id from onemoreapp_users where username = '{Email}'")[0]
			context = User.objects.filter(email=Email)
			email = EmailMessage('Account password','your password is '+context[0].password, to=[Email])
			email.send()
			return HttpResponseRedirect(reverse('signin'))
		else:
			return HttpResponseRedirect(reverse('signin'))
	return render(request,"forgotpassword.html")

def needhelp(request):
	if request.method == "POST":
		need = need()
		need.name = request.POST['name']
		need.email = request.POST['email']
		need.contact = request.POST['contact']
		need.save()
	return render(request,"need.html")
