from django.shortcuts import render
from .models import projects
def home(request):
	return render(request,'index.html')

def about(request):
	proficiency=[
			'Proficient in Programming languages like Python, C++, JavaScript.',

			'Familiar with different Operating Systems specially debian based linux (kali).',

			'Good practical knowledge of Object Oriented Programming (OOP).',

			'Clear understanding of Relational Database, E-R Diagram, UML Class Diagram, Software Engineering principles.',

			'Practical knowledge of responsive design. Worked with HTML, CSS, JS etc.',

			'Worked with different frameworks, such as Django, Spring.',

			'Done Web Development, Android Development in university course projects.',
			
			'Familiar with different IDEs (Sublime-text, Eclipse, CodeBlocks, Visual Studio Code etc.).',

		]

	return render(request,'About.html',{'proficiency':proficiency})
		
def experience(request):
	return render(request,'Experience.html')

def portfolio(request):
	# django projects 
	djShoppingMall=projects()
	djShoppingMall.link= "https://github.com/MahmudJewel/E_commerce"
	djShoppingMall.title="Shopping Mall"
	djShoppingMall.desc="Django"
	djShoppingMall.img='../static/img/project-img/dj-shoppingMall.jpg'

	djBlog=projects()
	djBlog.link= "https://github.com/MahmudJewel/techvillain"
	djBlog.title="Blog site"
	djBlog.desc="Django"
	djBlog.img='../static/img/project-img/dj-blog.jpg'

	djGrocery=projects()
	djGrocery.link= "https://github.com/MahmudJewel/Juwel-Mahmud_iTQAN-Django-Task"
	djGrocery.title="Grocery Shop"
	djGrocery.desc="Django"
	djGrocery.img='../static/img/project-img/dj-grocery1.jpg'

	djOnlineExam=projects()
	djOnlineExam.link= "https://github.com/MahmudJewel/online_exam"
	djOnlineExam.title="Online Exam"
	djOnlineExam.desc="Django"
	djOnlineExam.img='../static/img/project-img/dj-onlineExam.jpg'

	djPortfolio=projects()
	djPortfolio.link= "https://github.com/MahmudJewel/portfolioWithDjango"
	djPortfolio.title="Portfolio-Django"
	djPortfolio.desc="Django"
	djPortfolio.img='../static/img/project-img/dj-portfolio.jpg'

	djWeather=projects()
	djWeather.link= "https://github.com/MahmudJewel/Weather"
	djWeather.title="Weather Detector"
	djWeather.desc="Django"
	djWeather.img='../static/img/project-img/dj-weather.png'

	djTodo=projects()
	djTodo.link= "https://github.com/MahmudJewel/ToDoApps"
	djTodo.title="ToDoApps"
	djTodo.desc="Django"
	djTodo.img='../static/img/project-img/dj-todo.jpg'

	djTakingNotes=projects()
	djTakingNotes.link= "https://github.com/MahmudJewel/notes-taking"
	djTakingNotes.title="Taking Notes"
	djTakingNotes.desc="Django"
	djTakingNotes.img='../static/img/project-img/dj-takingnotes.jpg'

	djStudentForm=projects()
	djStudentForm.link= "https://github.com/MahmudJewel/studentForm"
	djStudentForm.title="Student Form"
	djStudentForm.desc="Django"
	djStudentForm.img='../static/img/project-img/dj-st.jpg'


	djFamouseQuotes=projects()
	djFamouseQuotes.link= "https://github.com/MahmudJewel/Quotes"
	djFamouseQuotes.title="Famous Quotes"
	djFamouseQuotes.desc="Django"
	djFamouseQuotes.img='../static/img/project-img/dj-quotes.jpg'

	drfEcommerceBackend=projects()
	drfEcommerceBackend.link= "https://github.com/MahmudJewel/E-commerce_backend"
	drfEcommerceBackend.title="E-commerce Backend"
	drfEcommerceBackend.desc="Django & Rest Framework"
	drfEcommerceBackend.img='../static/img/project-img/drf-ecom-backend.jpg'


	# Django+React / Vuejs projects
	reangoTodo=projects()
	reangoTodo.link= "https://github.com/MahmudJewel/Reango_task_management"
	reangoTodo.title="Task mngmt using Django, React & DRF"
	reangoTodo.desc="Django,React & DRF"
	reangoTodo.img='../static/img/project-img/reango-Task.jpg'
	
	vuengoTodo=projects()
	vuengoTodo.link= "https://github.com/MahmudJewel/Todo-DRF-Vuejs"
	vuengoTodo.title="ToDo using Django, Vuejs & DRF"
	vuengoTodo.desc="Django,Vuejs & DRF"
	vuengoTodo.img='../static/img/project-img/vuengo-toDo.jpg'
	
	vuengoCRUD=projects()
	vuengoCRUD.link= "https://github.com/MahmudJewel/CRUD-DRF-VUEJS"
	vuengoCRUD.title="CRUD using Django, Vuejs & DRF"
	vuengoCRUD.desc="Django,Vuejs & DRF"
	vuengoCRUD.img='../static/img/project-img/vuengo-Crud.jpg'
	
	# react projects 
	reactCal=projects()
	reactCal.link= "https://github.com/MahmudJewel/react-calculator"
	reactCal.title="React Calculator"
	reactCal.desc="React"
	reactCal.img='../static/img/project-img/react-calculator.jpg'

	reactForm=projects()
	reactForm.link= "https://github.com/MahmudJewel/react-form"
	reactForm.title="React Form"
	reactForm.desc="React"
	reactForm.img='../static/img/project-img/react-form.jpg'

	# Bootstrap projects 
	btEcommerce=projects()
	btEcommerce.link= "https://github.com/MahmudJewel/E_commerce-frontend"
	btEcommerce.title="E-commerce"
	btEcommerce.desc="Bootstrap"
	btEcommerce.img='../static/img/project-img/bt-shoppingmall.png'

	btBlog=projects()
	btBlog.link= "https://github.com/MahmudJewel/techvillain-frontend"
	btBlog.title="Blog site"
	btBlog.desc="Bootstrap"
	btBlog.img='../static/img/project-img/bt-techVillain.png'

	btGrocery=projects()
	btGrocery.link= "https://github.com/MahmudJewel/Juwel-Mahmud_iTQAN-Django-Task"
	btGrocery.title="Grocery Shop"
	btGrocery.desc="Bootstrap"
	btGrocery.img='../static/img/project-img/bt-groceryShop.png'

	btOnlineExam=projects()
	btOnlineExam.link= "https://github.com/MahmudJewel/online_exam_screenshot"
	btOnlineExam.title="Exam Portal"
	btOnlineExam.desc="Bootstrap"
	btOnlineExam.img='../static/img/project-img/bt-onlineExam.png'

	# javascript projects 
	jsPortfolio=projects()
	jsPortfolio.link= "https://github.com/MahmudJewel/portfolio"
	jsPortfolio.title="Portfolio"
	jsPortfolio.desc="JavaScript"
	jsPortfolio.img='../static/img/project-img/js-portfolio.jpg'

	jsRandomQuotes=projects()
	jsRandomQuotes.link= "https://mahmudjewel.github.io/Random-Quotes/"
	jsRandomQuotes.title="Random Quotes Generator"
	jsRandomQuotes.desc="JavaScript"
	jsRandomQuotes.img='../static/img/project-img/js-rq.jpg'


	jsMTable=projects()
	jsMTable.link= "https://mahmudjewel.github.io/Multplication-Table/"
	jsMTable.title="Multiplication Table"
	jsMTable.desc="JavaScript"
	jsMTable.img='../static/img/project-img/js-mt.jpg'

	jsBookList=projects()
	jsBookList.link= "https://mahmudjewel.github.io/Book-List/"
	jsBookList.title="Book List"
	jsBookList.desc="JavaScript"
	jsBookList.img='../static/img/project-img/js-booklist.jpg'

	# java projects 
	jvPharmacyStore=projects()
	jvPharmacyStore.link= "https://github.com/MahmudJewel/Pharmacy-Store-Management-System"
	jvPharmacyStore.title="Pharmacy Store Management System"
	jvPharmacyStore.desc="Java"
	jvPharmacyStore.img='../static/img/project-img/jv-pharmacy.jpg'


	jvFileTransfer=projects()
	jvFileTransfer.link= "https://github.com/MahmudJewel/File-transferring-app"
	jvFileTransfer.title="File Transferring app"
	jvFileTransfer.desc="Java"
	jvFileTransfer.img='../static/img/project-img/jv-file-transferring.jpg'


	dj_project_list=[
			djShoppingMall,
			djBlog,
			drfEcommerceBackend,
			djGrocery,
			djOnlineExam,
			djTodo,
			djPortfolio,
			djWeather,
			djTakingNotes,
			djFamouseQuotes,
			djStudentForm,
		]

	react_vuengo_project_list=[
			reangoTodo,
			vuengoTodo,
			vuengoCRUD,
		]

	react_project_list=[
			reactCal,
			reactForm,
		]

	js_project_list=[
			jsPortfolio,
			jsBookList,
			jsRandomQuotes,
			jsMTable
		]
	bootstrap_project_list=[
		btEcommerce,
		btBlog,
		btGrocery,
		btOnlineExam,
	]
 
	java_project_list=[
			jvPharmacyStore,
			jvFileTransfer,
		]
	
	context= {
		'dj_project_list': dj_project_list,
		'react_vuengo_project_list': react_vuengo_project_list,
		'react_project_list': react_project_list,
		'js_project_list' : js_project_list,
		'bootstrap_project_list': bootstrap_project_list,
		'java_project_list': java_project_list,
	}

	return render(request,'Portfolio.html',context)

def services(request):
	return render(request,'Services.html')
		
def contact(request):
	return render(request,'Contact.html')
		