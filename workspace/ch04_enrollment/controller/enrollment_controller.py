from flask import render_template, request, redirect, url_for, jsonify, Blueprint
from service.lecture_service import LectureService
from service.enrollment_service import EnrollmentService
from service.student_service import StudentService
from service.course_service import CourseService
from service.enrollment_service import EnrollmentDB
from service.professor_service import ProfessorService
from service.lecture_service import LectureService


enrollment_blueprint = Blueprint('enrollment', __name__)
student_service = StudentService()
course_service = CourseService()
professor_service = ProfessorService()
lecture_service = LectureService()
enrollment_service = EnrollmentService()



@enrollment_blueprint.route("/")
def index():
    return render_template('index.html')

@enrollment_blueprint.route("/student_management", methods=["GET", "POST"])
def student_management():
    if request.method == "GET":
        students = student_service.get_student()
        return render_template('student_management.html', students=students)
    if request.method == "POST":
        number = request.form['number']
        name = request.form['name']
        gender = request.form['gender']
        student_service.add_student(number, name, gender)
        return redirect(url_for("enrollment.student_management"))


@enrollment_blueprint.route("/course_management", methods=["GET", "POST"])
def course_management():
    if request.method == "GET":
        courses = course_service.get_course()
        return render_template("course_management.html", courses=courses)
    if request.method == "POST":
        name = request.form['name']
        credit = request.form['credit']
        course_service.add_course(name, credit)
        return redirect(url_for("enrollment.course_management"))

@enrollment_blueprint.route("/enrollment_management", methods=["GET", "POST"])
def enrollment_management():
    students = student_service.get_student()
    courses = course_service.get_course()
    enrollments = enrollment_service.get_enrollment()
    return render_template("enrollment_management.html", students=students, courses=courses, enrollments = enrollments)

@enrollment_blueprint.route("/register_enrollment", methods=["POST"])
def enrollment_add():
    student_id = request.form['student_id']
    course_id = request.form['course_id']
    enrollment_service.add_enrollment(student_id, course_id)
    return redirect(url_for("enrollment.enrollment_management"))

@enrollment_blueprint.route("/professor_management", methods=["GET", "POST"])
def professor_management():
    if request.method == "GET":
        professors = professor_service.get_professor()
        return render_template("professor_management.html", professors=professors)
    elif request.method == "POST":
        name = request.form['professor_name']
        major = request.form['major']
        email = request.form['email']
        professor_service.add_professor(name, major, email)
        return redirect(url_for("enrollment.professor_management"))


@enrollment_blueprint.route("/lecture_management", methods=["GET", "POST"])
def lecture_management():
    if request.method == "GET":
        lectures = lecture_service.get_lecture()
        professors = professor_service.get_professor()
        courses = course_service.get_course()
        lectureList = lecture_service.get_lectuerList()
        return render_template("lecture_management.html", lectures=lectures, professors=professors, courses=courses, lectureList=lectureList)
    elif request.method == "POST":
        professor_id = request.form.get('professor_id')
        course_id = request.form['course_id']
        day = request.form['day']
        start_time = request.form['start_time']
        lecture_service.add_lecture(professor_id, course_id, day, start_time)
        return redirect(url_for("enrollment.lecture_management"))


@enrollment_blueprint.route("/api/lecture_list")
def lecture_list():
    lectures = lecture_service.get_lectuerList()
    response = jsonify(lectures)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response