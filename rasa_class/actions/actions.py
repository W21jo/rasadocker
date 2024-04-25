from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
import sqlite3
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
from rasa_sdk.executor import CollectingDispatcher
# from sqlalchemy import create_engine, Column, String, Integer
# from sqlalchemy.ext.declarative import declarative_base
import json
import os
from sqlite3 import Error
import logging
from rasa_sdk.types import DomainDict
# from rasa.core.channels.channel import InputChannel, OutputChannel, UserMessage
# from rasa.core.channels.channel import CollectingOutputChannel
# from rasa.core.channels.console import ConsoleInputChannel
# from sanic import Sanic, Blueprint, response
# from rasa.core.agent import Agent
# from rasa.core.interpreter import RasaNLUInterpreter
# from rasa.utils.endpoints import EndpointConfig




# from.import course
# from.import sub

# from flask import Flask, jsonify, request
# from flask_cors import CORS



# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "http://localhost:5005"}})

# # Your Rasa actions and other routes here

# if __name__ == "__main__":
#     app.run(debug=True)





# class ActionAskName(Action):

#     def name(self) -> Text:
#         return "action_ask_name"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(response="utter_ask_name")

#         return []


# class ActionAskEmpCode(Action):

#     def name(self) -> Text:
#         return "action_ask_empcode"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(response="utter_ask_empcode")

#         return []


# class ActionAskEmail(Action):

#     def name(self) -> Text:
#         return "action_ask_email"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(response="utter_ask_email")

#         return []


# class ActionSaveDetails(Action):

#     def name(self) -> Text:
#         return "action_save_candidate"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         Repo.insert(tracker.get_slot('PERSON'), tracker.get_slot('emp_code'), tracker.get_slot('email'))

#         dispatcher.utter_message(response="utter_display_details")

#         return []



# class ActionDeleteCandidate(Action):

#     def name(self) -> Text:
#         return "action_delete_candidate"

#     def run(self, dispatcher: CollecstingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         value = tracker.latest_message['entities'][0]['value']

#         Repo.delete(value)

#         dispatcher.utter_message(text="Deleted successfully")

#         return []
####################################################################### code 100

# class ActionCourse(Action):
        
#     def name(self) -> Text:
#             return "action_Course"
    

#     def run(self, dispatcher: CollectingDispatcher,
#                 tracker: Tracker,
#                 domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#             course_name = tracker.get_slot('course_name')

#             # Replace 'CourseDatabase' with the actual class name from your module
#             course_db = course()  

#             # Assuming 'select' is a method in your CourseDatabase class
#             rows = course_db.select(course_name)
#             print(f"Debugging: rows from the database: {rows}")


#             if rows:
#                 # Assuming your rows contain a description in the second column
#                 des = rows[0][0]
#                 dispatcher.utter_message(text=f"The course {course_name} covers various topics including {rows}.")
#             else:
#                 dispatcher.utter_message(text=f"Sorry, no information found for {course_name}.")

#             return []
    

# class ActionCourse_code(Action):
        
#     def name(self) -> Text:
#             return "action_Course_code"
    

#     def run(self, dispatcher: CollectingDispatcher,
#                 tracker: Tracker,
#                 domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#             course_code= tracker.get_slot('course_code')

#             # Replace 'CourseDatabase' with the actual class name from your module
#             course_db = sub()

#             # Assuming 'select' is a method in your CourseDatabase class
#             rows = course_db.select2(course_code)
#             print(f"Debugging: rows from the database: {rows}")


#             if rows:
#                 # Assuming your rows contain a description in the second column
#                 des = rows[0][0]
#                 dispatcher.utter_message(text=f"The course {course_code} covers various topics including {rows}.")
#             else:
#                 dispatcher.utter_message(text=f"Sorry, no information found for {course_code}.")

#             return []

    # def run(self, dispatcher: CollectingDispatcher,
    #             tracker: Tracker,
    #             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
    #         course_name = tracker.get_slot('course_name')
    #         rows = course.select(course_name)
    #         dispatcher.utter_message(text=rows)

    #         course_name = tracker.get_slot('course_name')

    #         # Replace 'CourseDatabase' with the actual class name from your module
    #         course_db = course()  

    #         # Assuming 'select' is a method in your CourseDatabase class
    #         rows = course.select(course_name)
    #         covers: {des}
    #         if rows:
    #         # Assuming your rows contain a description in the second column
    #             des = rows[0][1]
    #             dispatcher.utter_message(text=f"The course {course_name}")
    #         else:
    #             dispatcher.utter_message(text=f"Sorry, no information found for {des}")

    #         return []
            # if rows:
            #     print(rows)
            # else:
            #     print("No records found.")
            # dispatcher.utter_message(response=" utter_course_name {rows} ")
            # dispatcher.utter_message(text=f"hi {rows}!")
            # if rows:
            #         logging.info(f"Found records: {rows}")
            #         dispatcher.utter_message(response="utter_course_name", rows=rows)
            #         dispatcher.utter_message(text=f"Hi {rows}!")
            # else:
            #         logging.warning("No records found.")
            #         dispatcher.utter_message(response="utter_no_records")

            # return []



# class ActionSayShirtSize(Action):

#     def name(self) -> Text:
#         return "action_say_shirt_size"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         shirt_size = tracker.get_slot("shirt_size")
#         if not shirt_size:
#             dispatcher.utter_message(text="I don't know your shirt size.")
#         else:
#             dispatcher.utter_message(text=f"Your shirt size is {shirt_size}!")
#         return []
# class ActionSayName(Action):

#     def name(self) -> Text:
#         return "action_say_name"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         name = tracker.get_slot("name")
#         if not name:
#             dispatcher.utter_message(text="I don't know your name .")
#         else:
#             dispatcher.utter_message(text=f"Your shirt size is {name}!")
#         return []

class ActionCheckStudentID(Action):
    def name(self) -> Text:
        return "action_check_student_id"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Get the student ID from the user's message
        student_id = tracker.latest_message.get('entities')[0]['value']  # Assuming the entity is properly extracted

        # Simulating a check with a predefined set of registered student IDs
        registered_student_ids = {'12345', '67890', '54321', '98765'}

        if student_id in registered_student_ids:
            dispatcher.utter_message(text="Your student ID is registered.")
        else:
            dispatcher.utter_message(text="Your student ID is not registered.")

        return []

# class ActionCheckStudentID(Action):
#     def name(self) -> Text:
#         return "action_check_student_id"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Get the student ID from the user's message
#         student_id = tracker.latest_message.get('text')

#         # Replace this logic with your actual student affairs database check
#         # Simulating the check with a predefined set of registered student IDs
#         registered_student_ids = set(['12345', '67890', '54321', '98765'])

#         if student_id in registered_student_ids:
#             dispatcher.utter_message(response="utter_student_id_registered")
#         else:
#             dispatcher.utter_message(response="utter_student_id_not_registered")

#         return []
    
# class ActionCheckStudentID(Action):
#     def name(self) -> Text:
#         return "action_check_student_id"

#     def run(
#         self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
#     ) -> List[Dict[Text, Any]]:
#         # Get the student ID from the user's message
#         student_id = tracker.latest_message.get("text")

#         # Simulate the check with a predefined set of registered student IDs
#         registered_student_ids = {"12345", "67890", "54321", "98765"}

#         if student_id in registered_student_ids:
#             dispatcher.utter_message(response="utter_student_id_registered")
#         else:
#             dispatcher.utter_message(response="utter_student_id_not_registered")

#         return []



# class ActionReturnName(Action):
#     def name(self) -> Text:
#         return "action_return_name"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Get the name slot value from the tracker
#         name = tracker.get_slot("name")

#         # Check if the name slot has a value
#         if name:
#             # Respond with the stored name
#             dispatcher.utter_message(f" Welcome {name}.")
#         else:
#             # If the name slot is not set, respond with a default message
#             dispatcher.utter_message("I don't have a name. Please provide a name.")

#         return []
    
# class ActionGetCourseDetails(Action):
#     def __init__(self):
#         super().__init__()

#         # Set up a connection to your SQLite database in the constructor
#         DATABASE_URL = "sqlite:///C:/Users/woeod/Desktop/sql_rasa/course_catalog.db"
#         self.engine = create_engine(DATABASE_URL)
#         self.Session = sessionmaker(bind=self.engine)

#     def name(self) -> Text:
#         return "action_get_course_details"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Extract the course code from the user's message
#         course_code = tracker.latest_message['text']

#         # Use the session to query the SQLite database
#         session = self.Session()

#         # Fetch course details from the 'courses' table
#         course_details = session.execute("SELECT * FROM courses WHERE course_code=?", (course_code,)).fetchone()

#         # Close the session
#         session.close()

#         if course_details:
#             response = f"Course Code: {course_details[0]}\nCourse Name: {course_details[1]}\nInstructor: {course_details[2]}\nSchedule: {course_details[3]}"
#         else:
#             response = "Sorry, I couldn't find information for that course code."

#         # Send the course details to the user
#         dispatcher.utter_message(text=response)

#         return []
    

# class CalculateGPA(Action):
#     def name(self) -> Text:
#         return "action_calculate_gpa"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         # Retrieve the intent entities
#         entities = tracker.latest_message['entities']
        
#         # Initialize variables for GPA calculation
#         total_grade_points = 0
#         total_credits = 0

#         # Check if GPA is provided
#         gpa_entity = next((entity for entity in entities if entity['entity'] == 'gpa'), None)
#         if gpa_entity:
#             gpa = float(gpa_entity['value'])
#             dispatcher.utter_message(f"Your GPA is {gpa:.3f}")
#             return []

#         # GPA not provided, proceed to calculate GPA from grade and credits
#         for entity in entities:
#             if entity['entity'] == 'grades':
#                 grade = entity['value']
#             elif entity['entity'] == 'credits':
#                 credits = int(entity['value'])
#                 # Calculate grade points
#                 if grade.upper() == 'A':
#                     grade_points = 4.0
#                 elif grade.upper() == 'A+':
#                     grade_points = 4.3
#                 elif grade.upper() == 'A-':
#                     grade_points = 3.7
#                 elif grade.upper() == 'B':
#                     grade_points = 3.0
#                 elif grade.upper() == 'B+':
#                     grade_points = 3.3
#                 elif grade.upper() == 'B-':
#                     grade_points = 2.7
#                 elif grade.upper() == 'C':
#                     grade_points = 2.0
#                 elif grade.upper() == 'C+':
#                     grade_points = 2.3
#                 elif grade.upper() == 'C-':
#                     grade_points = 1.7
#                 elif grade.upper() == 'D':
#                     grade_points = 1.0
#                 elif grade.upper() == 'D+':
#                     grade_points = 1.3
#                 elif grade.upper() == 'D-':
#                     grade_points = 0.7
#                 elif grade.upper() == 'F':
#                     grade_points = 0.0
#                 else:
#                     grade_points = 0.0  # Default to 0 for unrecognized grades
#                 # Update total grade points and total credits
#                 total_grade_points += grade_points * credits
#                 total_credits += credits
        
#         # Calculate GPA
#         if total_credits != 0:
#             gpa = total_grade_points / total_credits
#         else:
#             gpa = 0.0
        
#         # Respond with calculated GPA
#         dispatcher.utter_message(f"Your updated GPA is {gpa:.2f}")

#         return []
    
# class ActionCalculateGPA(Action):
#     def name(self) -> Text:
#         return "action_calculate_gpa"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         grades = tracker.get_slot("grades")
#         credits = tracker.get_slot("credits")
#         gpa = tracker.get_slot("gpa")

#         if not grades or not credits or gpa is None:
#             dispatcher.utter_message(text="Sorry, I couldn't retrieve your grades, credits, or old GPA.")
#             return []

#         total_quality_points = sum([grade_to_quality_point(grade) * credit for grade, credit in zip(grades, credits)])
#         total_credits = sum(credits)
#         calculated_gpa = (gpa * total_credits + total_quality_points) / (total_credits + sum(credits))

#         dispatcher.utter_message(text=f"Your new GPA is: {calculated_gpa:.2f}")
#         return []

# def grade_to_quality_point(grade: str) -> float:
#     # Define mapping of grades to quality points
#     grade_mapping = {
#         "A": 4.0,
#         "A-": 3.7,
#         "B+": 3.3,
#         "B": 3.0,
#         "B-": 2.7,
#         "C+": 2.3,
#         "C": 2.0,
#         "C-": 1.7,
#         "D+": 1.3,
#         "D": 1.0,
#         "F": 0.0
#     }
#     return grade_mapping.get(grade.upper(), 0.0)


# class ActionCalculateNewGPA(Action):
#     def name(self) -> Text:
#         return "action_calculate_new_gpa"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         # Get values of grade, points, and GPA from slots
#         gpa = tracker.get_slot("gpa")
#         grades = tracker.get_slot("grades")
#         points = tracker.get_slot("points")

#         if points and grades and gpa:
#             # Convert course points and GPA to float
#             total_grade_points = 0
#             total_points = 0

#             # Mapping of letter grades to GPA scale
#             grade_scale = {
#                 "A+": 4.0, "A": 4.0, "A-": 3.7,
#                 "B+": 3.3, "B": 3.0, "B-": 2.7,
#                 "C+": 2.3, "C": 2.0, "C-": 1.7,
#                 "D+": 1.3, "D": 1.0, "D-": 0.7,
#                 "F": 0.0
#             }

#             for grade, credit in zip(grades, points):
#                 # Calculate total grade points
#                 total_grade_points += grade_scale.get(grade.upper(), 0) * credit
#                 # Calculate total points
#                 total_points += credit

#             # Calculate new GPA
#             new_gpa = (float(gpa) * total_points + total_grade_points) / (total_points + sum(points))

#             # Print and dispatch new GPA
#             new_gpa_message = f"Your new GPA is: {new_gpa:.2f}"
#             print(new_gpa_message)
#             dispatcher.utter_message(text=new_gpa_message)

#         return []







class ActionCalculateNewGPA(Action):
    def name(self) -> Text:
        return "action_calculate_new_gpa"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get values of grade, credit, and GPA from slots
        grade = tracker.get_slot("gradestext")
        credit = tracker.get_slot("points")
        gpa = tracker.get_slot("gpa")

        print("Grade:", grade)
        print("Credit:", credit)
        print("Current GPA:", gpa)

        if grade and credit and gpa:
            # Ensure credit and GPA are converted to numeric types
            try:
                credit = float(credit)
                gpa = float(gpa)
            except (ValueError, TypeError):
                # Handle the case where credit or GPA cannot be converted to a float
                print("Error: Credit or GPA is not a valid number")
                return []

            # Mapping of letter grades to GPA scale
            grade_scale = {
                "A+": 4.0, "A": 4.0, "A-": 3.7,
                "B+": 3.3, "B": 3.0, "B-": 2.7,
                "C+": 2.3, "C": 2.0, "C-": 1.7,
                "D+": 1.3, "D": 1.0, "D-": 0.7,
                "F": 0.0
            }

            # Calculate grade points for the single course
            total_grade_points = grade_scale.get(grade.upper(), 0) * credit
            total_credits = credit

            # Calculate new GPA
            new_gpa = (gpa * total_credits + total_grade_points) / (total_credits + credit)

            # Print and dispatch new GPA
            new_gpa_message = f"Your new GPA is: {new_gpa:.2f}"
            print(new_gpa_message)
            dispatcher.utter_message(text=new_gpa_message)

        return []
    



# class ActionGetCourseDetails(Action):
#     def name(self) -> Text:
#         return "action_get_course_details"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         course_code = tracker.get_slot('course_code')
#         course_found = False

#         course_data = [
#     ('CE 201', 'Linear Circuit Analysis I', 3, 'This course covers the fundamentals of linear circuit analysis. Topics include resistive circuits, network theorems, and basic semiconductor devices. Lectures: 3 hours.'),
#     ('CE 207', 'Electronic Measurement Techniques Lab', 1, 'Hands-on laboratory course focusing on electronic measurement techniques. Lab sessions: 3 hours.'),
#     ('CE 202', 'Linear Circuit Analysis II', 3, 'Continuation of Linear Circuit Analysis I. Topics include AC analysis, frequency response, and advanced network theorems. Lectures: 3 hours.'),
#     ('CE 270', 'Introduction to Digital System Design', 4, 'Introduction to digital systems. Topics include digital logic design, combinational and sequential circuits, and digital system modeling. Lectures: 3 hours; Lab sessions: 3 hours.'),
#     ('CE 255', 'Introduction to Electronic Analysis and Design', 3, 'Introduction to electronic analysis and design. Topics include electronic components, amplifiers, and analog circuit design. Lectures: 3 hours.'),
#     ('CE 208', 'Electronic Devices and Design Laboratory', 1, 'Laboratory course focusing on electronic devices and design. Lab sessions: 3 hours.'),
#     # ('CE 301', 'Signals and Systems', 3, 'Introduction to signals and systems. Topics include signal representation, system properties, and Fourier analysis. Lectures: 3 hours.'),
#     # ('CE 264', 'Advanced C Programming', 3, 'Advanced programming course in the C language. Topics include data structures, algorithms, and software development. Lectures: 2 hours; Lab sessions: 2 hours.'),
#     # ('CE 362', 'Microprocessor Systems and Interfacing', 4, 'Introduction to microprocessor systems and interfacing. Topics include assembly language programming, interfacing techniques, and microprocessor applications. Lectures: 3 hours; Lab sessions: 3 hours.'),
#     # ('CE 368', 'Data Structures', 3, 'Introduction to data structures and algorithms. Topics include linked lists, trees, sorting, and searching. Lectures: 3 hours.'),
#     # ('CE 364', 'Software Engineering Tools Laboratory', 1, 'Laboratory course focusing on software engineering tools. Lab sessions: 3 hours.'),
#     # ('CE 302', 'Probabilistic Methods in Electrical and Computer Engineering', 3, 'Introduction to probabilistic methods in electrical and computer engineering. Topics include random variables, probability distributions, and statistical inference. Lectures: 3 hours.'),
#     # ('CE 200', 'Electrical and Computer Engineering Sophomore Seminar', 0, 'Sophomore Lect.: 1h'),
#     # ('CE 400', 'Professional Development and Career Guidance - Graduation Project I', 1, 'Pre: CE 200, Senior Lect.: 1h; Lab.: 1h'),
#     # ('CE 337', 'ASIC Design Laboratory', 2, 'Pre: EE 270 (min grade of C) or CE 270 (min grade of C) Lect.: 1h; Lab.: 3h'),
#     # ('CE 437', 'Computer Design and Prototyping', 4, 'Pre: CE 337, CE 362 Lect.: 3h; Lab.: 3h'),
#     # ('CE 468', 'Introduction to Compilers and Translation Engineering', 4, 'Pre: CE 362, CE 368 Lect.: 3h; Lab.: 2h'),
#     # ('CE 469', 'Operating System Engineering', 4, 'Pre: CE 368, CE 437 Lect.: 3h; Lab.: 3h'),
#     # ('CE 477', 'Digital Systems Senior Project', 4, 'Pre: CE 400 or EE 400, EE Core Curriculum or CE Core Curriculum, Senior Lect.: 1h; Lab.: 1h'),
#     # ('ENGR 297', 'Basic Mechanics I (Statics)', 3, 'Pre: PHYS 172, ConP: MA 261, Lect.: 3h\nDescription: This course introduces the principles of statics with a focus on basic mechanics.'),
#     # ('IE 335', 'Operation Research Optimization', 3, 'Pre: MA 265, ConP: EE 302 or CE 302 or IE 332, Lect.: 2h; Lab.: 2h\nDescription: Introduction to optimization techniques in operations research.'),
#     # ('IE 336', 'Operation Research  Stochastic Models', 3, 'Pre: MA 265, IE 230, ConP: EE 302 or CE 302 or IE 332, MA 266, Lect.: 3h\nDescription: This course explores stochastic models in operations research.'),
#     # ('ME 200', 'Thermodynamics I', 3, 'Pre: CHM 115, ConP: MA 261, ENGR 132, Lect.: 3h\nDescription: Fundamentals of thermodynamics with applications to engineering systems.'),
#     # ('MSE 230', 'Structure and Properties of Materials', 3, 'Pre: CHM 115 (min. grade C-), MA 165 (min grade C-), Lect.: 3h\nDescription: Study of the structure and properties of materials.'),
#     # ('NUCL 200', 'Introduction to Nuclear Engineering', 3, 'Pre: MA 166 or equivalent, PHYS 172 or equivalent, Lect.: 3h\nDescription: Introduction to nuclear engineering principles and applications.'),
#     # ('NANO 101', 'Introduction to Nanotechnology', 3, 'Pre: MA 261; MA 266 or MA 262; PHYS 272 or PHYS 241; CHM 115, Lect.: 3h\nDescription: Basic principles and applications of nanotechnology.'),
#     # ('CVL 355', 'Engineering Environmental Sustainability I', 3, 'Pre: Sophomore, Lect.: 3h\nDescription: Introduction to engineering approaches for environmental sustainability.'),
#     # ('MA 165', 'Analytic Geometry and Calculus I', 4, 'Passing Math Placement Test or MAT 110 or MA 158, Lect.: 3h; Lab.: 2h\nDescription: Fundamental calculus concepts, including limits and derivatives.'),
#     # ('MA 166', 'Analytic Geometry and Calculus II', 4, 'Pre: MA 165, Lect.: 4h\nDescription: Continuation of calculus concepts, including integrals and applications.'),
#     # ('MA 261', 'Multivariate Calculus', 4, 'Pre: MA 166, Lect.: 4h\nDescription: Study of calculus in multiple dimensions and vector analysis.'),
#     # ('MA 265', 'Linear Algebra', 3, 'Pre: MA 166, Lect.: 3h\nDescription: Introduction to linear algebra and its applications.'),
#     # ('MA 266', 'Ordinary Differential Equations', 3, 'Pre: MA 261, Lect.: 3h\nDescription: Study of ordinary differential equations and their solutions.'),
#     # ('MA 369', 'Discrete Mathematics for Computer Engineering', 3, 'Pre: CE 270, Lect.: 3h\nDescription: Introduction to discrete mathematics with applications in computer engineering.'),
#     # ('CHM 115', 'General Chemistry I', 4, 'Pre: MA 165, Lect.: 3h; Recitation: 1h\nDescription: Introduction to the principles of chemistry, including atomic structure, bonding, and reactions.'),
#     # ('PHYS 172', 'Modern Mechanics', 4, 'Pre: MA 165, Lect.: 3h; Recitation: 1h\nDescription: Study of classical mechanics with applications to modern physics.'),
#     # ('PHYS 272', 'Physics III: Vibrations, Waves, Optics, and Modern Physics', 4, 'Pre: MA 166, PHYS 241; Coreq: MA 261; Co-enrollment: MA 261, Lect.: 3h; Lab.: 3h\nDescription: Study of vibrations, waves, optics, and modern physics.'),
#     # ('ECON 251', 'Principles of Microeconomics', 3, 'Pre: MA 15800 or MA 16010 or MA 16020, Lect.: 3h\nDescription: Introduction to microeconomic principles and theory.'),
#     # ('ECON 252', 'Principles of Macroeconomics', 3, 'Pre: MA 15800 or MA 16010 or MA 16020, Lect.: 3h\nDescription: Introduction to macroeconomic principles and theory.'),
#     # ('SOC 100', 'Introductory Sociology', 3, 'Lect.: 3h\nDescription: Introduction to sociological concepts and methods.'),
#     # ('PSY 120', 'Elementary Psychology', 3, 'Lect.: 3h\nDescription: Introduction to basic principles and concepts of psychology.'),
# ]

# # Now you can access the course data using course_data[index]
# # For example:
#         print(course_data[0])  # Output: ('CE 201', 'Linear Circuit Analysis I', 3, 'This course covers the fundamentals of linear circuit analysis. Topics include resistive circuits, network theorems, and basic semiconductor devices. Lectures: 3 hours.')


#         # if course_code:
#         #     course_found = False
#         #     for course in course_data:
#         #         if course_code.lower() == course[0].lower():
#         #             dispatcher.utter_message(text=f"**Course Name:** {course[1]}\n**Course Code:** {course[0]}\n**Credit Hours:** {course[2]}\n**Description:** {course[3]}")
#         #             course_found = True
#         #             break
            
#         #     if not course_found:
#         #         dispatcher.utter_message(text="Sorry, I couldn't find information about that course.")
#         # else:
#         #     dispatcher.utter_message(text="Please provide a course code.")
#         def find_course(course_code):
#             for course in course_data:
#                 if course_code.lower() == course[0].lower():
#                     return f"**Course Name:** {course[1]}\n**Course Code:** {course[0]}\n**Credit Hours:** {course[2]}\n**Description:** {course[3]}"
#             return "Sorry, I couldn't find information about that course."

#         async def search_course_info(request, dispatcher):
#             course_code = request.get('course_code')
#             if course_code:
#                 course_info = find_course(course_code)
#                 dispatcher.utter_message(text=course_info)
#             else:
#                 dispatcher.utter_message(text="Please provide a course code.")


#         return []



from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGetCourseDetails(Action):git add rasa_class/

    def name(self) -> Text:
        return "action_get_course_details"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        course_code = tracker.get_slot('course_code')

        def find_course(course_code):
            course_data = [
                ('CE 201', 'Linear Circuit Analysis I', 3, 'This course covers the fundamentals of linear circuit analysis. Topics include resistive circuits, network theorems, and basic semiconductor devices. Lectures: 3 hours.'),
                ('CE 207', 'Electronic Measurement Techniques Lab', 1, 'Hands-on laboratory course focusing on electronic measurement techniques. Lab sessions: 3 hours.'),
                ('CE 202', 'Linear Circuit Analysis II', 3, 'Continuation of Linear Circuit Analysis I. Topics include AC analysis, frequency response, and advanced network theorems. Lectures: 3 hours.'),
                ('CE 270', 'Introduction to Digital System Design', 4, 'Introduction to digital systems. Topics include digital logic design, combinational and sequential circuits, and digital system modeling. Lectures: 3 hours; Lab sessions: 3 hours.'),
                ('CE 255', 'Introduction to Electronic Analysis and Design', 3, 'Introduction to electronic analysis and design. Topics include electronic components, amplifiers, and analog circuit design. Lectures: 3 hours.'),
                ('CE 208', 'Electronic Devices and Design Laboratory', 1, 'Laboratory course focusing on electronic devices and design. Lab sessions: 3 hours.'),
                ('CE 301', 'Signals and Systems', 3, 'Introduction to signals and systems. Topics include signal representation, system properties, and Fourier analysis. Lectures: 3 hours.'),
                ('CE 264', 'Advanced C Programming', 3, 'Advanced programming course in the C language. Topics include data structures, algorithms, and software development. Lectures: 2 hours; Lab sessions: 2 hours.'),
                ('CE 362', 'Microprocessor Systems and Interfacing', 4, 'Introduction to microprocessor systems and interfacing. Topics include assembly language programming, interfacing techniques, and microprocessor applications. Lectures: 3 hours; Lab sessions: 3 hours.'),
                ('CE 368', 'Data Structures', 3, 'Introduction to data structures and algorithms. Topics include linked lists, trees, sorting, and searching. Lectures: 3 hours.'),
                ('CE 364', 'Software Engineering Tools Laboratory', 1, 'Laboratory course focusing on software engineering tools. Lab sessions: 3 hours.'),
                ('CE 302', 'Probabilistic Methods in Electrical and Computer Engineering', 3, 'Introduction to probabilistic methods in electrical and computer engineering. Topics include random variables, probability distributions, and statistical inference. Lectures: 3 hours.'),
                ('CE 200', 'Electrical and Computer Engineering Sophomore Seminar', 0, 'Sophomore Lect.: 1h'),
                ('CE 400', 'Professional Development and Career Guidance - Graduation Project I', 1, 'Pre: CE 200, Senior Lect.: 1h; Lab.: 1h'),
                ('CE 337', 'ASIC Design Laboratory', 2, 'Pre: EE 270 (min grade of C) or CE 270 (min grade of C) Lect.: 1h; Lab.: 3h'),
                ('CE 437', 'Computer Design and Prototyping', 4, 'Pre: CE 337, CE 362 Lect.: 3h; Lab.: 3h'),
                ('CE 468', 'Introduction to Compilers and Translation Engineering', 4, 'Pre: CE 362, CE 368 Lect.: 3h; Lab.: 2h'),
                ('CE 469', 'Operating System Engineering', 4, 'Pre: CE 368, CE 437 Lect.: 3h; Lab.: 3h'),
                ('CE 477', 'Digital Systems Senior Project', 4, 'Pre: CE 400 or EE 400, EE Core Curriculum or CE Core Curriculum, Senior Lect.: 1h; Lab.: 1h'),
                ('ENGR 297', 'Basic Mechanics I (Statics)', 3, 'Pre: PHYS 172, ConP: MA 261, Lect.: 3h\nDescription: This course introduces the principles of statics with a focus on basic mechanics.'),
                ('IE 335', 'Operation Research Optimization', 3, 'Pre: MA 265, ConP: EE 302 or CE 302 or IE 332, Lect.: 2h; Lab.: 2h\nDescription: Introduction to optimization techniques in operations research.'),
                ('IE 336', 'Operation Research  Stochastic Models', 3, 'Pre: MA 265, IE 230, ConP: EE 302 or CE 302 or IE 332, MA 266, Lect.: 3h\nDescription: This course explores stochastic models in operations research.'),
                ('ME 200', 'Thermodynamics I', 3, 'Pre: CHM 115, ConP: MA 261, ENGR 132, Lect.: 3h\nDescription: Fundamentals of thermodynamics with applications to engineering systems.'),
                ('MSE 230', 'Structure and Properties of Materials', 3, 'Pre: CHM 115 (min. grade C-), MA 165 (min grade C-), Lect.: 3h\nDescription: Study of the structure and properties of materials.'),
                ('NUCL 200', 'Introduction to Nuclear Engineering', 3, 'Pre: MA 166 or equivalent, PHYS 172 or equivalent, Lect.: 3h\nDescription: Introduction to nuclear engineering principles and applications.'),
                ('NANO 101', 'Introduction to Nanotechnology', 3, 'Pre: MA 261; MA 266 or MA 262; PHYS 272 or PHYS 241; CHM 115, Lect.: 3h\nDescription: Basic principles and applications of nanotechnology.'),
                ('CVL 355', 'Engineering Environmental Sustainability I', 3, 'Pre: Sophomore, Lect.: 3h\nDescription: Introduction to engineering approaches for environmental sustainability.'),
                ('MA 165', 'Analytic Geometry and Calculus I', 4, 'Passing Math Placement Test or MAT 110 or MA 158, Lect.: 3h; Lab.: 2h\nDescription: Fundamental calculus concepts, including limits and derivatives.'),
                ('MA 166', 'Analytic Geometry and Calculus II', 4, 'Pre: MA 165, Lect.: 4h\nDescription: Continuation of calculus concepts, including integrals and applications.'),
                ('MA 261', 'Multivariate Calculus', 4, 'Pre: MA 166, Lect.: 4h\nDescription: Study of calculus in multiple dimensions and vector analysis.'),
                ('MA 265', 'Linear Algebra', 3, 'Pre: MA 166, Lect.: 3h\nDescription: Introduction to linear algebra and its applications.'),
                ('MA 266', 'Ordinary Differential Equations', 3, 'Pre: MA 261, Lect.: 3h\nDescription: Study of ordinary differential equations and their solutions.'),
                ('MA 369', 'Discrete Mathematics for Computer Engineering', 3, 'Pre: CE 270, Lect.: 3h\nDescription: Introduction to discrete mathematics with applications in computer engineering.'),
                ('CHM 115', 'General Chemistry I', 4, 'Pre: MA 165, Lect.: 3h; Recitation: 1h\nDescription: Introduction to the principles of chemistry, including atomic structure, bonding, and reactions.'),
                ('PHYS 172', 'Modern Mechanics', 4, 'Pre: MA 165, Lect.: 3h; Recitation: 1h\nDescription: Study of classical mechanics with applications to modern physics.'),
                ('PHYS 272', 'Physics III: Vibrations, Waves, Optics, and Modern Physics', 4, 'Pre: MA 166, PHYS 241; Coreq: MA 261; Co-enrollment: MA 261, Lect.: 3h; Lab.: 3h\nDescription: Study of vibrations, waves, optics, and modern physics.'),
                ('ECON 251', 'Principles of Microeconomics', 3, 'Pre: MA 15800 or MA 16010 or MA 16020, Lect.: 3h\nDescription: Introduction to microeconomic principles and theory.'),
                ('ECON 252', 'Principles of Macroeconomics', 3, 'Pre: MA 15800 or MA 16010 or MA 16020, Lect.: 3h\nDescription: Introduction to macroeconomic principles and theory.'),
                ('SOC 100', 'Introductory Sociology', 3, 'Lect.: 3h\nDescription: Introduction to sociological concepts and methods.'),
                ('PSY 120', 'Elementary Psychology', 3, 'Lect.: 3h\nDescription: Introduction to basic principles and concepts of psychology.'),            ]
            for course in course_data:
                if course_code.lower() == course[0].lower():
                    return f"**Course Name:** {course[1]}\n**Course Code:** {course[0]}\n**Credit Hours:** {course[2]}\n**Description:** {course[3]}"
            return "Sorry, I couldn't find information about that course."

        if course_code:
            course_info = find_course(course_code)
            dispatcher.utter_message(text=course_info)
        else:
            dispatcher.utter_message(text="Please provide a course code.")

        return []
   