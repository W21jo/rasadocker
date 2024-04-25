# import sqlite3

# conn = sqlite3.connect('sub.db')

# class sub:
#         # Connect to the SQLite database (replace 'your_database.db' with your actual database file)
#     conn = sqlite3.connect('sub.db')
#     cursor = conn.cursor()

#             # Create the courses table
#     cursor.execute('''
#                 CREATE TABLE IF NOT EXISTS courses (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     course_code TEXT NOT NULL,
#                     course_name TEXT NOT NULL,
#                     credits INTEGER,
#                     description TEXT
#                 );
#             ''')



#     course_data = [
#                 ('CE 201', 'Linear Circuit Analysis I', 3, 'This course covers the fundamentals of linear circuit analysis. Topics include resistive circuits, network theorems, and basic semiconductor devices. Lectures: 3 hours.'),
#                 ('CE 207', 'Electronic Measurement Techniques Lab', 1, 'Hands-on laboratory course focusing on electronic measurement techniques. Lab sessions: 3 hours.'),
#                 ('CE 202', 'Linear Circuit Analysis II', 3, 'Continuation of Linear Circuit Analysis I. Topics include AC analysis, frequency response, and advanced network theorems. Lectures: 3 hours.'),
#                 ('CE 270', 'Introduction to Digital System Design', 4, 'Introduction to digital systems. Topics include digital logic design, combinational and sequential circuits, and digital system modeling. Lectures: 3 hours; Lab sessions: 3 hours.'),
#                 ('CE 255', 'Introduction to Electronic Analysis and Design', 3, 'Introduction to electronic analysis and design. Topics include electronic components, amplifiers, and analog circuit design. Lectures: 3 hours.'),
#                 ('CE 208', 'Electronic Devices and Design Laboratory', 1, 'Laboratory course focusing on electronic devices and design. Lab sessions: 3 hours.'),
#                 ('CE 301', 'Signals and Systems', 3, 'Introduction to signals and systems. Topics include signal representation, system properties, and Fourier analysis. Lectures: 3 hours.'),
#                 ('CE 264', 'Advanced C Programming', 3, 'Advanced programming course in the C language. Topics include data structures, algorithms, and software development. Lectures: 2 hours; Lab sessions: 2 hours.'),
#                 ('CE 362', 'Microprocessor Systems and Interfacing', 4, 'Introduction to microprocessor systems and interfacing. Topics include assembly language programming, interfacing techniques, and microprocessor applications. Lectures: 3 hours; Lab sessions: 3 hours.'),
#                 ('CE 368', 'Data Structures', 3, 'Introduction to data structures and algorithms. Topics include linked lists, trees, sorting, and searching. Lectures: 3 hours.'),
#                 ('CE 364', 'Software Engineering Tools Laboratory', 1, 'Laboratory course focusing on software engineering tools. Lab sessions: 3 hours.'),
#                 ('CE 302', 'Probabilistic Methods in Electrical and Computer Engineering', 3, 'Introduction to probabilistic methods in electrical and computer engineering. Topics include random variables, probability distributions, and statistical inference. Lectures: 3 hours.'),
#                 ('CE 200', 'Electrical and Computer Engineering Sophomore Seminar', 0, 'Sophomore Lect.: 1h'),
#                 ('CE 400', 'Professional Development and Career Guidance - Graduation Project I', 1, 'Pre: CE 200, Senior Lect.: 1h; Lab.: 1h'),
#                 ('CE 337', 'ASIC Design Laboratory', 2, 'Pre: EE 270 (min grade of C) or CE 270 (min grade of C) Lect.: 1h; Lab.: 3h'),
#                 ('CE 437', 'Computer Design and Prototyping', 4, 'Pre: CE 337, CE 362 Lect.: 3h; Lab.: 3h'),
#                 ('CE 468', 'Introduction to Compilers and Translation Engineering', 4, 'Pre: CE 362, CE 368 Lect.: 3h; Lab.: 2h'),
#                 ('CE 469', 'Operating System Engineering', 4, 'Pre: CE 368, CE 437 Lect.: 3h; Lab.: 3h'),
#                 ('CE 477', 'Digital Systems Senior Project', 4, 'Pre: CE 400 or EE 400, EE Core Curriculum or CE Core Curriculum, Senior Lect.: 1h; Lab.: 1h'),
#                     ('ENGR 297', 'Basic Mechanics I (Statics)', 3, 'Pre: PHYS 172, ConP: MA 261, Lect.: 3h\nDescription: This course introduces the principles of statics with a focus on basic mechanics.'),
#     ('IE 335', 'Operation Research Optimization', 3, 'Pre: MA 265, ConP: EE 302 or CE 302 or IE 332, Lect.: 2h; Lab.: 2h\nDescription: Introduction to optimization techniques in operations research.'),
#     ('IE 336', 'Operation Research  Stochastic Models', 3, 'Pre: MA 265, IE 230, ConP: EE 302 or CE 302 or IE 332, MA 266, Lect.: 3h\nDescription: This course explores stochastic models in operations research.'),
#     ('ME 200', 'Thermodynamics I', 3, 'Pre: CHM 115, ConP: MA 261, ENGR 132, Lect.: 3h\nDescription: Fundamentals of thermodynamics with applications to engineering systems.'),
#     ('MSE 230', 'Structure and Properties of Materials', 3, 'Pre: CHM 115 (min. grade C-), MA 165 (min grade C-), Lect.: 3h\nDescription: Study of the structure and properties of materials.'),
#     ('NUCL 200', 'Introduction to Nuclear Engineering', 3, 'Pre: MA 166 or equivalent, PHYS 172 or equivalent, Lect.: 3h\nDescription: Introduction to nuclear engineering principles and applications.'),
#     ('NANO 101', 'Introduction to Nanotechnology', 3, 'Pre: MA 261; MA 266 or MA 262; PHYS 272 or PHYS 241; CHM 115, Lect.: 3h\nDescription: Basic principles and applications of nanotechnology.'),
#     ('CVL 355', 'Engineering Environmental Sustainability I', 3, 'Pre: Sophomore, Lect.: 3h\nDescription: Introduction to engineering approaches for environmental sustainability.'),
#     ('MA 165', 'Analytic Geometry and Calculus I', 4, 'Passing Math Placement Test or MAT 110 or MA 158, Lect.: 3h; Lab.: 2h\nDescription: Fundamental calculus concepts, including limits and derivatives.'),
#     ('MA 166', 'Analytic Geometry and Calculus II', 4, 'Pre: MA 165, Lect.: 4h\nDescription: Continuation of calculus concepts, including integrals and applications.'),
#     ('MA 261', 'Multivariate Calculus', 4, 'Pre: MA 166, Lect.: 4h\nDescription: Study of calculus in multiple dimensions and vector analysis.'),
#     ('MA 265', 'Linear Algebra', 3, 'Pre: MA 166, Lect.: 3h\nDescription: Introduction to linear algebra and its applications.'),
#     ('MA 266', 'Ordinary Differential Equations', 3, 'Pre: MA 261, Lect.: 3h\nDescription: Study of ordinary differential equations and their solutions.'),
#     ('MA 369', 'Discrete Mathematics for Computer Engineering', 3, 'Pre: CE 270, Lect.: 3h\nDescription: Introduction to discrete mathematics with applications in computer engineering.'),
#     ('CHM 115', 'General Chemistry I', 4, 'ConP: MA 165, Lect.: 3h; Lab.: 2h\nDescription: Fundamentals of general chemistry with laboratory work.'),
#     ('PHYS 172', 'Modern Mechanics', 4, 'ConP: MA 165, Lect.: 3h; Lab.: 2h\nDescription: Study of classical mechanics and motion.'),
#     ('PHYS 272', 'Electric and Magnetic Interactions', 4, 'Pre: PHYS 172, ConP: MA 166, Lect.: 3h; Lab.: 2h\nDescription: Introduction to electric and magnetic interactions.'),
#     ('BIOL 110', 'Fundamentals of Biology I', 4, 'Lect.: 3h; Lab.: 2h\nDescription: Introduction to the fundamental principles of biology.'),
#     ('CHM 116', 'General Chemistry II', 4, 'Pre: CHM 115, Lect.: 3h; Lab.: 2h\nDescription: Continuation of general chemistry principles and laboratory work.'),
#     ('PHYS 322', 'Intermediate Optics', 3, 'Pre: PHYS 272 or PHYS 241, Lect.: 3h\nDescription: Study of intermediate optical principles.'),
#     ('PHYS 342', 'Modern Physics', 3, 'Pre: PHYS 272 or PHYS 241, Lect.: 3h\nDescription: Introduction to modern physics concepts and theories.'),
#     ('BIOL 121', 'Biology I: Diversity, Ecology, and Behavior', 2, 'Lect.: 2h\nDescription: Study of biological diversity, ecology, and behavior.'),
#     ('CHM 112', 'General Chemistry', 3, 'Pre: CHM 115, Lect.: 3h\nDescription: General chemistry principles.'),
#     ('EAPS 125', 'Environmental Science and Conservation', 3, 'Lect.: 3h\nDescription: Study of environmental science and conservation principles.'),
#     ('ENGL 100', 'English for Academic Studies', 3, 'Lect.: 3h\nDescription: Development of English language skills for academic studies.'),
#     ('ENGL 106', 'First-Year Composition', 4, 'Pre: ENGL 100, Lect.: 4h\nDescription: Composition and rhetoric skills for academic writing.'),
#     ('EE 201', 'Linear Circuit Analysis I', 3, 'Introduction to linear circuit analysis with a focus on DC circuits.'),
#     ('EE 202', 'Linear Circuit Analysis II', 3, 'Advanced study of linear circuit analysis, with an emphasis on AC circuits.'),
#     ('EE 207', 'Electronic Measurement Techniques Lab', 1, 'Laboratory course covering electronic measurement techniques.'),
#     ('EE 208', 'Electronic Devices and Design Laboratory', 1, 'Hands-on experience in designing electronic devices.'),
#     ('EE 255', 'Introduction to Electronic Analysis and Design', 3, 'Fundamentals of electronic circuits, analysis, and design.'),
#     ('EE 270', 'Introduction to Digital System Design', 4, 'Study of digital systems design, including combinational and sequential logic.'),
#     ('EE 301', 'Signals and Systems', 3, 'Introduction to signals and systems, including time and frequency domain analysis.'),
#     ('EE 302', 'Probabilistic Methods in Electrical and Computer Engineering', 3, 'Application of probabilistic methods in electrical and computer engineering.'),
#     ('EE 311', 'Electric and Magnetic Fields', 3, 'Study of electric and magnetic fields with applications in electrical engineering.'),
#     ('EE 200', 'Electrical and Computer Engineering Sophomore Seminar', 0, 'Sophomore seminar in Electrical and Computer Engineering. Lectures for 1 hour.'),
#     ('EE 400', 'Professional Development and Career Guidance - Graduation Project I', 1, 'Professional development and career guidance course with a focus on Graduation Project I. Lectures for 1 hour; Lab for 1 hour.'),
#     ('CHE 200', 'Chemical Engineering Sophomore Seminar', 1, 'Sophomore Lect.: 1h'),
#     ('CHE 205', 'Chemical Engineering Calculations', 4, 'Pre: ENGR 131, PHYS 172, MA 165, ConP: CHM 116 Lect.: 3h; Lab: 2h Min Passing grade C'),
#     ('CHE 211', 'Introductory Chemical Engineering Thermodynamics', 4, 'Pre: CHE 205, MA 261 Lect.: 3h; Lab: 2h'),
#     ('CHE 300', 'Chemical Engineering Junior Seminar', 1, 'Pre: CHE 200, Junior Lect.: 1h'),
#     ('CHE 306', 'Design of Staged Separation Processes', 3, 'Pre: CHE 211 Lect.: 3h; Lab: 2h'),
#     ('CHE 320', 'Statistical Modeling and Quality Enhancement', 3, 'Pre: CHE 205, ConP: MA 265 Lect.: 3h; Lab: 2h'),
#     ('CHE 348', 'Chemical Reaction Engineering', 4, 'Pre: CHE 211, MA 265, MA 266, ConP: CHM 261 Lect.: 3h; Lab:2h'),
#     ('CHE 377', 'Momentum Transfer', 4, 'Pre: CHE 211, ConP: MA 266 Lect.: 3h; Lab:2h'),
#     ('CHE 378', 'Heat and Mass Transfer', 4, 'Pre: CHE 211, CHE 377 Lect.: 3h; Lab:2h'),
#     ('CHE 400', 'Chemical Engineering Senior Seminar', 1, 'Pre: CHE 300, Senior ConP: CHE 456 Lect.: 1h'),
#     ('CHE 420', 'Process Safety Management', 3, 'ConP: CHE 348, CHE 378. Lect.: 3h'),
#     ('CHE 435', 'Chemical Engineering Laboratory', 4, 'Pre: CHE 306, CHE 320, CHE 348, CHE 378. Lect.: 2h; Lab: 3h'),
#     ('CHE 456', 'Process Dynamics and Control', 3, 'Pre: CHE 377. ConP: CHE 348, CHE 378. Lect.: 3h; Lab: 2h'),
#     ('CHE 450', 'Design and Analysis of Processing Systems', 4, 'Pre: CHE 306, CHE 378, CHE 400. ConP: CHE 435. Lect.: 2h; Lab: 2h'),
#     ('CHM 261', 'Organic Chemistry I', 3, 'Pre: CHM 116. Lect.: 3h'),
#     ('CHM 262', 'Organic Chemistry II', 3, 'Pre: CHM 261. Lect.: 3h'),
#     ('CHM 263', 'Organic Chemistry Laboratory I', 1, 'ConP: CHM 261. Lab: 3h'),
#     ('CHM 264', 'Organic Chemistry Laboratory II', 1, 'Pre: CHM 263. ConP: CHM 262. Lab: 3h'),
#     ('CHM 370', 'Topics in Physical Chemistry', 3, 'Pre: CHE 211, MA 261, PHYS 241, CHM 116. Lect.: 3h'),
#         ('ME 270', 'Basic Mechanics I', 3, 'Pre: PHYS 172 (min. grade C-), MA 166 (min. grade C-); ConP: MA 261, ENGR 132. Lect.: 3h'),
#     ('ME 274', 'Basic Mechanics II', 3, 'Pre: ME 270, ENGR 132 (C-). ConP: MA 262. Lect.: 3h'),
#     ('ME 323', 'Mechanics Of Materials', 3, 'Pre: ME 270. Lect.: 3h'),
#     ('MSE 230', 'Structure and Properties of Materials', 3, 'Pre: CHM 115 (min. grade C-), MA 165 (min grade C-). Lect.: 3h'),
#     ('ME 290', 'Global Engineering Professional Seminar', 1, 'Pre: COM 114, ENGL 106. Lect.: 1h'),
#     ('EE 201', 'Linear Circuit Analysis I', 3, 'Pre: ENGR 131, PHYS 172, MA 166 (min grade C-). ConP: MA 261. Lect.: 3h'),
#     ('EE 207', 'Electronic Measurement Techniques Lab', 1, 'ConP: EE 201. Lab.: 3h'),
#     ('ME 365', 'Systems and Measurements', 3, 'Pre: EE 201, ME 274, MA 262, EE 207. Lect.: 2h; Lab: 2h'),
#     ('ME 375', 'System Modeling and Analysis', 3, 'Pre: ME 365, MA 303. Lect.: 3h'),
#     ('ME 200', 'Thermodynamics I', 3, 'Pre: CHM 115. ConP: MA 261, ENGR 132. Lect.: 3h'),
#     ('ME 309', 'Fluid Mechanics', 4, 'Pre: ME 263, ME 274, MA 262. Lect.: 3h; Lab: 2h'),
#     ('ME 315', 'Heat and Mass Transfer', 4, 'Pre: ME 309, ME 365, MA 303. Lect.: 3h; Lab: 2h'),
#     ('ME 263', 'Introduction to Mechanical Engineering Design, Innovation and Entrepreneurship', 3, 'Pre: ME 270, COM 114, ENGL 106, ENGR 132. ConP: ME200, MA 262, ME 290, CGT 163. Lect.:2h; Lab: 2h'),
#     ('ME 352', 'Machine Design I', 4, 'Pre: ME 263, ME 274 and ME 323. Lect.:3h; Lab: 2h'),
#     ('ME 463', 'Engineering Design', 3, 'Pre: ME 352, MSE 230. ConP: ME 315, ME 375. Lect.:1; Lab: 2h'),
#     ('ME 300', 'Thermodynamics II', 3, 'Pre: ME 200, ME 263. Lect.: 3h'),
#     ('ME 452', 'Machine Design II', 3, 'Pre: ME 352, MSE 230. Lect.: 3h'),
#     ('ME 475', 'Automatic Control Systems', 3, 'Pre: ME 375. Lect.: 2h; Lab: 2h'),
#     ('IE 300', 'Industrial Engineering Seminar', 1, 'Senior Lect.: 1h; Lab: 1h'),
#     ('IE 230', 'Probability and Statistics in Engineering I', 3, 'ConP: MA 261. Lect.: 3h; Lab: 1h'),
#     ('IE 330', 'Probability and Statistics in Engineering II', 3, 'Pre: IE 230. Lect.: 3h; Lab: 1h'),
#     ('IE 332', 'Computing in Industrial Engineering', 3, 'Pre: ENGR 131, CS 159. ConP: IE 330. Lect.: 2h; Lab: 2h'),
#     ('IE 335', 'Operations Research - Optimization', 3, 'Pre: MA 265. ConP: EE 302 or CE 302 or IE 332. Lect.: 2h; Lab: 2h'),
#     ('IE 336', 'Operations Research - Stochastic Models', 3, 'Pre: MA 265, IE 230. ConP: EE 302 or CE 302 or IE 332, MA 266. Lect.: 3h'),
#     ('IE 343', 'Engineering Economics', 3, 'Pre: ENGR 131, MA 166. Lect.: 3h'),
#     ('IE 370', 'Manufacturing Processes I', 3, 'Pre: NUCL 273. Lect.: 3h'),
#     ('IE 383', 'Integrated Production Systems I', 3, 'Pre: IE 335. Lect.: 3h'),
#     ('IE 386', 'Work Analysis and Design I', 3, 'Pre: IE 330. Lect.: 2h; Lab: 2h'),
#     ('IE 431', 'Industrial Engineering Design', 3, 'Pre: IE 300, all 300 level IE courses, Senior. Lect.: 1h; Lab: 1h'),
#     ('IE 474', 'Industrial Control Systems', 3, 'Pre: CS 159, EE 201, MA 265, MA 266, ME 270. Lect.: 3h'),
#     ('CNIT 180', 'Introduction to Systems Development', 3, 'Pre: PC Literacy. Lect.: 2h; Lab: 2h'),
#     ('CNIT 155', 'Introduction to Object-Oriented Programming', 3, 'Pre: PC Literacy. Lect.: 2h; Lab: 2h'),
#     ('CNIT 176', 'Information Technology Architecture', 3, 'Pre: PC Literacy. Lect.: 3h'),
#     ('CNIT 255', 'Programming for the Internet', 3, 'Pre: CNIT 155 (C-). Lect.: 2h; Lab: 2h'),
#     ('CNIT 272', 'Database Fundamentals', 3, 'Pre: CNIT 155 (C-), CNIT 180 (C-). Lect.: 2h; Lab: 2h'),
#     ('CNIT 242', 'System Administration', 3, 'Pre: CNIT 176 (C-), Sophomore. Lect.: 2h; Lab: 2h'),
#     ('CNIT 280', 'Systems Analysis and Design methods', 3, 'Pre: CNIT 180 (C-), CNIT 272 (C-). Lect.: 3h'),
#     ('CNIT 380', 'Advanced Analysis and Design', 4, 'Pre: CNIT 280 (C-). Lect.: 3h; Lab: 2h'),
#     ('CNIT 480', 'Managing Information Technology Projects', 3, 'Pre: CNIT 280 (C-), Senior. Lect.: 3h'),
#     ('CNIT 315', 'Systems Programming', 3, 'Pre: CNIT 255 (C-). Lect.: 2h; Lab: 2h'),
#     ('CNIT 325', 'Object-Oriented Application Development', 3, 'Pre: CNIT 255 (C-). Lect.: 2h; Lab: 2h'),
#     ('CNIT 372', 'Database Programming', 3, 'Pre: CNIT 272 (C-). Lect.: 2h; Lab: 2h'),
#     ('CNIT 392', 'Enterprise Data Management', 3, 'Pre: CNIT 272 (C-). Lect.: 2h; Lab: 2h'),
#         ('CNIT 399', 'Topics In Computer and Information Technology - Graduation Project I', 3, 'Senior. Lect.: 1h; Lab: 1h'),
#     ('CNIT 499', 'Topics In Computer and Information Technology - Graduation Project II', 3, 'Pre: CNIT 399 (C-). Lect.: 1h; Lab: 1h'),
#         ('ACT 300', 'Financial Accounting', 3, 'Pre: MAT 100 or MAT 200 or MA 223. Lect.: 3h'),
#     ('ACT 200', 'Introductory Accounting For Non-Business Majors', 3, 'Pre: MAT 150 or MA 223 or MA 165. Lect.: 3h'),
#     ('STAT 225', 'Introduction To Probability Models', 3, 'Pre: MA 224. Lect.: 3h; Lab: 2h'),
#     ('STAT 301', 'Elementary Statistical Methods', 3, 'Pre: MA 224 or MA 165 or equivalent. Lect.: 3h; Lab: 2h'),
#         ('IT 450', 'Production Cost Analysis', 3, 'Pre: MA 223. Lect.: 3h'),
#     ('ACT 310', 'Managerial Accounting', 3, 'Pre: ACT 300. Lect.: 3h'),
#     ('FIN 300', 'Managerial Finance', 3, 'Pre: ACT 300, Sophomore. Lect.: 3h'),
#     ('IT 345', 'Automatic Identification And Data Capture', 3, 'Junior. Lect.: 2h; Lab: 2h'),
#     ('MKT 300', 'Principles of Marketing Management', 3, 'Sophomore. Lect.: 3h'),
#     ('MGMT 323', 'Introduction To Market Analysis', 3, 'Pre: ECON 252. Lect.: 3h'),
#     ('BUS 220', 'Business Law and Ethics', 3, 'Pre: BUS 250. Lect.: 3h'),
#     ('OLS 484', 'Leadership Strategies for Quality and Productivity', 3, 'Pre: IT 342 or STAT 301. Lect.: 3h'),
#     ('IT 342', 'Introduction to Statistical Quality', 3, 'Pre: MA 223. Lect.: 3h; Lab: 2h'),
#     ('BUS 250', 'Business Organization and Management', 3, 'Pre: ENGL 100. Lect.: 3h'),
#     ('ENTR 200', 'Introduction To Entrepreneurship And Innovation', 3, '- Lect.: 3h'),
#     ('ENTR 310', 'Marketing and Management for New Ventures', 3, 'Pre: ENTR 200. Lect.: 3h'),
#     ('HRM 300', 'Organizational Behavior', 3, 'Pre: BUS 250, Sophomore. Lect.: 3h'),
#     ('HRM 340', 'Human Resource Management', 3, 'Pre: HRM 300. Lect.: 3h'),
#         ('MA 223', 'Introductory Analysis I', 3, 'Passing ENG Math Placement test or MAT 110 or MA 158. Lect.: 3h'),
#     ('MA 224', 'Introductory Analysis II', 3, 'Pre: MA 223. Lect.: 3h')
    

# #     ('COM 114', 'Fundamentals of Speech Communication', 3, 'Pre: ENGL 100, Lect.: 3h\nDescription: Fundamentals of ,
# # speech communication and public speaking.')
# #     ('EE201', 'Linear Circuit Analysis I', 3, 'Introduction to linear circuit analysis and basic principles of electrical circuits.'),
# # ('EE 202', 'Linear Circuit Analysis II', 3, 'Continuation of Linear Circuit Analysis I with a focus on more advanced topics.'),
# # ('EE 207', 'Electronic Measurement Techniques Lab', 1, 'Hands-on laboratory experience with electronic measurement techniques.'),
# # ('EE 208', 'Electronic Devices and Design Laboratory', 1, 'Laboratory work on electronic devices and design principles.'),
# # ('EE 255', 'Introduction to Electronic Analysis and Design', 3, 'Introduction to electronic circuits analysis and design fundamentals.'),
# # ('EE 270', 'Introduction to Digital System Design', 4, 'Fundamentals of digital system design and implementation.'),
# # ('EE 301', 'Signals and Systems', 3, 'Introduction to signals and systems in electrical engineering.'),
# # ('EE 302', 'Probabilistic Methods in Electrical and Computer Engineering', 3, 'Application of probabilistic methods in electrical and computer engineering.'),
# # ('EE 311', 'Electric and Magnetic Fields', 3, 'Study of electric and magnetic fields in electrical engineering applications.'),
# # ('EE 305', 'Semiconductor Devices', 3, 'Understanding and analysis of semiconductor devices in electronic circuits.'),
# # ('EE 321', 'Electromechanical Motion Devices', 3, 'Analysis and design of electromechanical motion devices in electrical systems.'),
# # ('EE 382', 'Feedback System Analysis and Design', 3, 'Study of feedback systems and their analysis and design principles.'),
# # ('EE 438', 'Digital Signal Processing with Applications', 4, 'Introduction to digital signal processing and its practical applications.'),
# # ('EE 440', 'Transmission of Information', 4, 'Study of information transmission in communication systems.'),
# # ('CE 362', 'Microprocessor Systems and Interfacing', 4, 'Design and interfacing of microprocessor systems for various applications.'), 
# # ('EE 400', 'Professional Development and Career Guidance - Graduation Project I', 1, 'Guidance and project work for professional development in electrical engineering.'),
# # ('EE 402', 'Electrical Engineering Design Projects', 3, 'Design projects for senior electrical engineering students.'),
# # ('CE 477', 'Digital Systems Senior Project', 4, 'Senior project focusing on digital systems for computer engineering students.')
# # ('IE 300', 'Industrial Engineering Seminar', 1, 'Senior seminar for industrial engineering students. Lectures: 1h; Lab: 1h.'),
# # ('IE 230', 'Probability and Statistics in Engineering I', 3, 'Introduction to probability and statistics in engineering. Lectures: 3h; Lab: 1h. Prerequisite: MA 261.'),
# # ('IE 330', 'Probability and Statistics in Engineering II', 3, 'Advanced topics in probability and statistics. Lectures: 3h; Lab: 1h. Prerequisite: IE 230.'),
# # ('IE 332', 'Computing in Industrial Engineering', 3, 'Introduction to computing in industrial engineering. Lectures: 2h; Lab: 2h. Prerequisites: ENGR 131, CS 159; Corequisite: IE 330.'),
# # ('IE 335', 'Operations Research - Optimization', 3, 'Introduction to optimization in operations research. Lectures: 2h; Lab: 2h. Prerequisite: MA 265; Corequisite: EE 302 or CE 302 or IE 332.'),
# # ('IE 336', 'Operations Research - Stochastic Models', 3, 'Introduction to stochastic models in operations research. Lectures: 3h. Prerequisites: MA 265, IE 230; Corequisite: EE 302 or CE 302 or IE 332, MA 266.'),
# # ('IE 343', 'Engineering Economics', 3, 'Introduction to engineering economics. Lectures: 3h. Prerequisites: ENGR 131, MA 166.'),
# # ('IE 370', 'Manufacturing Processes I', 3, 'Introduction to manufacturing processes. Lectures: 3h. Prerequisite: NUCL 273.'),
# # ('IE 383', 'Integrated Production Systems I', 3, 'Introduction to integrated production systems. Lectures: 3h. Prerequisite: IE 335.'),
# # ('IE 386', 'Work Analysis and Design I', 3, 'Introduction to work analysis and design. Lectures: 2h; Lab: 2h. Prerequisite: IE 330.'),
# # ('IE 431', 'Industrial Engineering Design', 3, 'Design projects in industrial engineering. Lectures: 1h; Lab: 1h. Prerequisite: IE 300, all 300 level IE courses, Senior.'),
# # ('IE 474', 'Industrial Control Systems', 3, 'Introduction to industrial control systems. Lectures: 3h. Prerequisites: CS 159, EE 201, MA 265, MA 266, ME 270.'), ('ME200', 'Thermodynamics I', 3, 'Introduction to thermodynamics principles. Lectures: 3h. Prerequisites: CHM 115; Corequisites: MA 261, ENGR 132.'),
# # ('ME 270', 'Basic Mechanics', 3, 'Introduction to basic mechanics. Lectures: 3h. Prerequisite: PHYS 172.'),
# # ('NUCL 273', 'Mechanics of Materials', 3, 'Study of mechanics of materials. Lectures: 3h. Prerequisite: ME 270.'),('ME270', 'Basic Mechanics I', 3, 'Introduction to basic mechanics. Lectures: 3h.'),
# # ('ME 274', 'Basic Mechanics II', 3, 'Advanced topics in basic mechanics. Lectures: 3h.'),
# # ('ME 323', 'Mechanics Of Materials', 3, 'Introduction to mechanics of materials. Lectures: 3h.') 
# # ('MSE 230', 'Structure and Properties of Materials', 3, 'Introduction to the structure and properties of materials. Lectures: 3h.')



#             ]

#     cursor.executemany('''
#             INSERT INTO courses (course_code, course_name, credits, description)
#             VALUES (?, ?, ?, ?);
#             ''', course_data)


#             # # Commit the changes and close the connection
#     conn.commit()

#     def select2(self,course_code):

#                     cursor = conn.cursor()

#                     cursor.execute('''
#                     SELECT * FROM courses WHERE course_code = ?;
#                         ''', (course_code,))
#                     rows = cursor.fetchall()
#                     query_result1 = rows[0][1]
#                     query_result2 = rows[0][2]
#                     query_result3 = rows[0][3]
#                     query_result4 = rows[0][4] 
#                     # if rows:
#                     #     query_result1 = rows[0][1]
#                     #     query_result2 = rows[0][2]
#                     #     query_result3 = rows[0][3]
#                     #     query_result4 = rows[0][4]
#                     # else:
#                     # # Handle the case when no rows are returned by the query i add it to cancel errors
#                     #     query_result1 = None
#                     #     query_result2 = None
#                     #     query_result3 = None
#                     #     query_result4 = None



                    
#                 #     query_result = [('Course code',query_result1), ('Course name',query_result2), ('credits',query_result3), ('description',query_result4)]  
#                     query_result = [
#                     ('Course code',   query_result1),
#                         ('Course name',   query_result2),
#                         ('Credits',       query_result3),
#                         ('Description',   query_result4)
#                         ]
#                 #     for aspect, result in query_result:
#                 #                 print(f"{aspect}: {result}")
#                     formatted_output = "\n".join([f"{aspect}: {result}" for aspect, result in query_result])

#                     return formatted_output
#     conn.close()