from django.shortcuts import render

# Create your views here.
def home(request):
  
  students = [
    {
      'name': 'Omar',
      'age': 23,
      'city': 'Cairo',
      'Occupation': 'Software Engineer',
      'active': True,
    }
    ,
    {
      'name': 'Mohamed',
      'age': 25,
      'city': 'Alexandria',
      'Occupation': 'Cybersecurity Engineer',
      'active': False,
    },
    {
      'name': 'Ahmed',
      'age': 24,
      'city': 'Giza',
      'Occupation': 'Machine Learning & AI Engineer',
      'active': True,
    },
    {
      'name': 'Ibrahimn',
      'age': 26,
      'city': 'Tanta',
      'Occupation': 'Data Scientist',
      'active': True,
    }
    
  ]
  context = {
    'name' : 'Omar',
    'age' : 23,
    'city' : 'Cairo',
    'Occupation' : 'Software Engineer',
    'students' : students,
    'page_title' : 'Home Page',
  }
  return render(request, 'home.html', context)
def about(request):
  context = {
    'page_title' : 'About Us',
  }
  return render(request, 'about.html')
def contact(request):
  context = {
    'page_title' : 'Contact Us',
  }
  return render(request, 'contact.html')
def Doctors(request):
  Doctors = [
    {
      'name': 'Omar',
      'city': 'Cairo',
      'Occupation': 'Psychaitrist',
    },
    {
      'name': 'Mohamed',
      'city': 'Alexandria',
      'Occupation': 'Psychologist',
      
    },
    {
      'name': 'Ahmed',
      'city': 'Giza',
      'Occupation': 'Neurologist',
      
    },
    {
      'name': 'Ibrahimn',
      'city': 'Tanta',
      'Occupation': 'Dentist',
      
    }
  ]
  context = {
    'page_title': 'Doctors',
    'Doctors': Doctors,
  }
  return render(request, 'Doctors.html', context)