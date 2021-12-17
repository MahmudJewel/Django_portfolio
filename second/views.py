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
	djShoppingMall=projects()
	djShoppingMall.link= "https://github.com/MahmudJewel/E_commerce"
	djShoppingMall.title="Shopping Mall"
	djShoppingMall.desc="Django Project"
	djShoppingMall.img='../static/img/project-img/dj-shoppingMall.jpg'

	djBlog=projects()
	djBlog.link= "https://github.com/MahmudJewel/techvillain"
	djBlog.title="Personal Blog(tech villain)"
	djBlog.desc="Django Project"
	djBlog.img='../static/img/project-img/dj-blog.jpg'

	djOnlineExam=projects()
	djOnlineExam.link= "https://github.com/MahmudJewel/online_exam"
	djOnlineExam.title="Online Exam"
	djOnlineExam.desc="Django Project"
	djOnlineExam.img='../static/img/project-img/dj-onlineExam.jpg'

	reactCal=projects()
	reactCal.link= "https://github.com/MahmudJewel/react-calculator"
	reactCal.title="React Calculator"
	reactCal.desc="React Project"
	reactCal.img='../static/img/project-img/react-calculator.jpg'

	jsPortfolio=projects()
	jsPortfolio.link= "https://github.com/MahmudJewel/portfolio"
	jsPortfolio.title="Portfolio"
	jsPortfolio.desc="JavaScript Project"
	jsPortfolio.img='../static/img/project-img/js-portfolio.jpg'

	djPortfolio=projects()
	djPortfolio.link= "https://github.com/MahmudJewel/portfolioWithDjango"
	djPortfolio.title="Portfolio-Django"
	djPortfolio.desc="Django Project"
	djPortfolio.img='../static/img/project-img/dj-portfolio.jpg'

	djWeather=projects()
	djWeather.link= "https://github.com/MahmudJewel/Weather"
	djWeather.title="Weather Detector"
	djWeather.desc="Django Project"
	djWeather.img='../static/img/project-img/dj-weather.png'

	djTodo=projects()
	djTodo.link= "https://github.com/MahmudJewel/ToDoApps"
	djTodo.title="ToDoApps"
	djTodo.desc="Django Project"
	djTodo.img='../static/img/project-img/dj-todo.jpg'

	djTakingNotes=projects()
	djTakingNotes.link= "https://github.com/MahmudJewel/notes-taking"
	djTakingNotes.title="Taking Notes"
	djTakingNotes.desc="Django Project"
	djTakingNotes.img='../static/img/project-img/dj-takingnotes.jpg'

	djStudentForm=projects()
	djStudentForm.link= "https://github.com/MahmudJewel/studentForm"
	djStudentForm.title="Student Form"
	djStudentForm.desc="Django Project"
	djStudentForm.img='../static/img/project-img/dj-st.jpg'


	djFamouseQuotes=projects()
	djFamouseQuotes.link= "https://github.com/MahmudJewel/Quotes"
	djFamouseQuotes.title="Famous Quotes"
	djFamouseQuotes.desc="Django Project"
	djFamouseQuotes.img='../static/img/project-img/dj-quotes.jpg'


	jvPharmacyStore=projects()
	jvPharmacyStore.link= "https://github.com/MahmudJewel/Pharmacy-Store-Management-System"
	jvPharmacyStore.title="Pharmacy Store Management System"
	jvPharmacyStore.desc="Java Project"
	jvPharmacyStore.img='../static/img/project-img/jv-pharmacy.jpg'


	jvFileTransfer=projects()
	jvFileTransfer.link= "https://github.com/MahmudJewel/File-transferring-app"
	jvFileTransfer.title="File Transferring app"
	jvFileTransfer.desc="Java Project"
	jvFileTransfer.img='../static/img/project-img/jv-file-transferring.jpg'


	jsRandomQuotes=projects()
	jsRandomQuotes.link= "https://mahmudjewel.github.io/Random-Quotes/"
	jsRandomQuotes.title="Random Quotes Generator"
	jsRandomQuotes.desc="JavaScript Project"
	jsRandomQuotes.img='../static/img/project-img/js-rq.jpg'


	jsMTable=projects()
	jsMTable.link= "https://mahmudjewel.github.io/Multplication-Table/"
	jsMTable.title="Multiplication Table"
	jsMTable.desc="JavaScript Project"
	jsMTable.img='../static/img/project-img/js-mt.jpg'

	jsBookList=projects()
	jsBookList.link= "https://mahmudjewel.github.io/Book-List/"
	jsBookList.title="Book List"
	jsBookList.desc="JavaScript Project"
	jsBookList.img='../static/img/project-img/js-booklist.jpg'

	apps=[
			djShoppingMall,
			djBlog,
			djOnlineExam,
			reactCal,
			jsPortfolio,
			djTodo,
			djPortfolio,
			djWeather,
			djTakingNotes,
			djFamouseQuotes,
			djStudentForm,
			jvPharmacyStore,
			jvFileTransfer,
			jsBookList,
			jsRandomQuotes,
			jsMTable
		]

	return render(request,'Portfolio.html',{ 'apps':apps} )

def services(request):
	return render(request,'Services.html')
		
def contact(request):
	return render(request,'Contact.html')
		