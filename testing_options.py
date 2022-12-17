# Options for testing course_finder.py

import course_finder

# ---- 'Department' Argument Options ----
#
#  CS
#  AAS
#  CHEM
#  BIOL
#  ECON 
#  ECE 

# ---- 'Instructor' Argument Options ----
#
#  CS instructors: ['Craig Dill', 'Luther Tychonievich', 'Upsorn Praphamontripong', 'James Cohoon', 'Ahmed Ibrahim', 
#                   'Mark Floryan', 'Collin/Cyrus', 'David Edwards+1', 'David Edwards', 'Nada Basit', 'Aaron Bloomfield', 
#                   'Thomas Horton', 'Gabriel Robins', 'Mary Smith', 'Charles Reiss', 'Samira Khan', 'Kong-Cheng Wong', 'Homa Alemzadeh', 
#                   'Andrew Grimshaw', 'Cameron Whitehouse', 'Connelly Barnes', 'Thomas Pinckney', 'Kevin Angstadt', 'Mark Sherriff']
#  
#  AAS instructors: ['Claudrena Harold', 'Kayla Kauffman', 'Tracie Canada', 'Lisa Shutt', 'Njelle Hamilton', 'Andrew Kahrl', 
#                   'Talitha LeFlouria', 'Julius Fleming', 'Sabrina Pendergrass', 'Aniko Bodroghkozy', 'Edwin Otu', 'Petal Samuel']
#  
#  CHEM instructors: ['Jennifer Maeng', 'David Metcalf', 'Lisa Morkowchuk', 'Kevin Welch', 'Linda Columbus', 'Diane Szaflarski', 
#                     'Laura Serbulea', 'Glenn McGarvey', 'Cassandra Fraser', 'Donald Hunt', 'Kateri DuBay', 'A Harrison', 'Barbara Venton', 
#                     'Brooks Pate', 'James Demas', 'James Landers', 'Cameron Mura', 'Staff', 'Timothy Macdonald', 'Sergei Egorov', 
#                     'Eric Herbst', 'Lin Pu', 'Michal Sabat', 'David Cafiso', 'Andreas Gahlmann', 'Rebecca Pompano', 'Kevin Lehmann', 'Marlit Hayslett']
#
#  BIOL instructors: ['Anna Way+1', 'Deforest Mellon', 'Michael Menaker', 'Jessamyn Manson+1', 'Jessamyn Manson', 'Israel Agorsor+1', 
#                     'FNU Kaushik Renganaath+1', 'Chun Su+1', 'W Wormington', 'Claire Cronmiller', 'Claire Cronmiller+1', 'Brittany Sutherland+1', 
#                     'Kimberly Arena+1', 'Martin Wu', '+1', 'David Kittlesen+1', 'Masashi Kawasaki', 'Mark Kopeny', 'Mark Kopeny+1', 
#                     'Akinleye Olajide Odeleye+1', 'Chhavi Sood+1', 'John Leonard+1', 'William Pearson', 'Jay Hirsh', 'Ignacio Provencio']
#  
#  ECON instructors: ['Carter Doyle', 'Xin Xue', 'Brett Lissenden', 'Niveditha Prabakaran', 'Ilhan Guner', 'Gang Zhang', 'Marc Santugini Repiquet', 'Siying Liu', 
#                     'Ramiro Burga Villanueva', 'Abiy Teshome', 'Lee Coppock', 'Miguel Mascarua Lara', 'Aidan Cochrane', 'Alexander Gross', 'Allison Luedtke', 
#                     'Jeffrey Schafer', 'Kelsey Booth', 'Melissa Moore', 'Grace Toufeili', 'Thomas West', 'Brett Fischer', 'Salim Ergene', 'Steven Marzagalli', 
#                     'Caroline Snead', 'Alexandra Schubert', 'Maria Winchell', 'Katherine Donnally', 'Ian Yanusko', 'Sarah Hill', 'Benjamin Hamilton', 
#                     'Hayden Goldberg', 'Benjamin Thomas', 'Lamiya Zaveri', 'Corey Bothwell', 'Andrew Kloosterman', 'Peter Troyan', 'Nathaniel Pattison']
#
#  ECE instructors: ['Scott Acton', 'Keith Williams', 'Joanne Dugan', 'James Adams+2', 'Harry Powell+1', 'Lloyd Harriott', 'Todd Delong', 'Andrea Vaccari+1', 
#                    'Avik Ghosh', 'Nathan Swami', 'Robert Weikle', 'Mircea Stan', 'Homa Alemzadeh', 'Ronald Williams', 'Cameron Whitehouse', 'Mona Zebarjadi', 
#                    'Jiaqi Gong', 'Steven Bowers', '+1', 'Gang Tao', 'Mool Gupta', 'Daniel Weller', 'Nicolas Barker', 'ShiZe Su+1', 'Farzad Farnoud', 
#                    'Gregory Lewin', 'Laura Barnes', 'Mustafa Sungkar+1', 'Stephen Wilson', 'Zongli Lin']


# ---- 'Class' Argument Options ----
#
#  CS Classes: ['CS 1010-001', 'CS 1110-001', 'CS 1110-002', 'CS 1110-100', 'CS 1110-101', 'CS 1110-102', 'CS 1110-103', 'CS 1110-104', 'CS 1110-105', 'CS 1110-106', 
#               'CS 1110-107', 'CS 1110-108', 'CS 1110-109', 'CS 1110-110', 'CS 1111-001', 'CS 1112-001', 'CS 1113-001', 'CS 1501-001', 'CS 1501-002', 'CS 1501-003', 
#               'CS 2102-001', 'CS 2102-002', 'CS 2110-001', 'CS 2110-002', 'CS 2110-003', 'CS 2110-101', 'CS 2110-102', 'CS 2110-103', 'CS 2110-104', 'CS 2150-001', 
#               'CS 2150-002', 'CS 2150-101', 'CS 2150-102', 'CS 2150-103', 'CS 2150-104', 'CS 2150-105', 'CS 2150-106', 'CS 2150-107', 'CS 2190-001', 'CS 3102-001', 
#               'CS 3205-001', 'CS 3205-002', 'CS 3240-001', 'CS 3240-101', 'CS 3240-102', 'CS 3330-001', 'CS 3330-002', 'CS 3330-101', 'CS 3330-102', 'CS 3330-103']
#
#  AAS Classes: ['AAS 1020-100', 'AAS 1020-101', 'AAS 1020-102', 'AAS 1020-103', 'AAS 1020-104', 'AAS 1020-105', 'AAS 1020-106', 'AAS 2224-001', 'AAS 2224-002', 'AAS 3500-001', 
#                'AAS 3500-002', 'AAS 3500-003', 'AAS 3500-004', 'AAS 3500-005', 'AAS 3500-006', 'AAS 3500-007', 'AAS 3652-001', 'AAS 3749-001', 'AAS 4109-001', 'AAS 4570-001']
#
#  CHEM Classes: ['CHEM 1400-001', 'CHEM 1410-100', 'CHEM 1410-101', 'CHEM 1420-100', 'CHEM 1420-101', 'CHEM 1420-102', 'CHEM 1420-103', 'CHEM 1420-200', 'CHEM 1420-201', 
#                 'CHEM 1420-202', 'CHEM 1420-203', 'CHEM 1420-300', 'CHEM 1420-301', 'CHEM 1420-500', 'CHEM 1420-501', 'CHEM 1420-600', 'CHEM 1420-601', 'CHEM 1420-602', 
#                 'CHEM 1420-603', 'CHEM 1421-001', 'CHEM 1421-002', 'CHEM 1421-003', 'CHEM 1421-004', 'CHEM 1421-005', 'CHEM 1421-006', 'CHEM 1421-007', 'CHEM 1421-008', 
#                 'CHEM 1421-009', 'CHEM 1421-010', 'CHEM 1421-011', 'CHEM 1421-012', 'CHEM 1421-013', 'CHEM 1421-014', 'CHEM 1421-015', 'CHEM 1421-016', 'CHEM 1421-017', 
#                 'CHEM 1421-018', 'CHEM 1421-019', 'CHEM 1421-020', 'CHEM 1421-021', 'CHEM 1421-022', 'CHEM 1421-023', 'CHEM 1421-024', 'CHEM 1421-025', 'CHEM 1421-026']
#
#  BIOL Classes: ['BIOL 1060-001', 'BIOL 1080-001', 'BIOL 1559-001', 'BIOL 2200-001', 'BIOL 2200-002', 'BIOL 2200-102', 'BIOL 2200-103', 'BIOL 2200-104', 'BIOL 2200-105', 
#                 'BIOL 2200-106', 'BIOL 2200-107', 'BIOL 2200-108', 'BIOL 2200-109', 'BIOL 2200-110', 'BIOL 2200-111', 'BIOL 2200-112', 'BIOL 2200-113', 'BIOL 2200-114', 
#                 'BIOL 2200-115', 'BIOL 2200-116', 'BIOL 2200-117', 'BIOL 2200-118', 'BIOL 2200-120', 'BIOL 2200-121', 'BIOL 2200-122', 'BIOL 2200-123', 'BIOL 2200-124', 
#                 'BIOL 2200-125', 'BIOL 2200-126', 'BIOL 2200-127', 'BIOL 2200-128', 'BIOL 2200-129', 'BIOL 2200-130', 'BIOL 2200-131', 'BIOL 2200-132', 'BIOL 2200-133', 
#                 'BIOL 2200-134', 'BIOL 3000-001', 'BIOL 3010-100', 'BIOL 3010-101', 'BIOL 3010-102', 'BIOL 3010-103', 'BIOL 3010-104', 'BIOL 3010-105', 'BIOL 3010-106']
#
#  ECON Classes: ['ECON 2010-100', 'ECON 2010-101', 'ECON 2010-108', 'ECON 2010-109', 'ECON 2010-110', 'ECON 2010-111', 'ECON 2010-112', 'ECON 2010-113', 'ECON 2010-114', 
#                 'ECON 2010-115', 'ECON 2010-116', 'ECON 2010-117', 'ECON 2010-118', 'ECON 2010-119', 'ECON 2010-120', 'ECON 2010-121', 'ECON 2010-200', 'ECON 2010-201', 
#                 'ECON 2010-202', 'ECON 2010-203', 'ECON 2010-204', 'ECON 2010-205', 'ECON 2010-206', 'ECON 2010-207', 'ECON 2010-208', 'ECON 2010-209', 'ECON 2020-001', 
#                 'ECON 2020-002', 'ECON 2020-100', 'ECON 2020-101', 'ECON 2020-102', 'ECON 2020-103', 'ECON 2020-104', 'ECON 2020-105', 'ECON 2020-106', 'ECON 2020-107', 
#                 'ECON 2020-108', 'ECON 2020-109', 'ECON 2020-110', 'ECON 2020-111', 'ECON 2020-112', 'ECON 2020-113', 'ECON 2020-114', 'ECON 2020-115', 'ECON 2020-116']
#
#  ECE Classes: ['ECE 2066-100', 'ECE 2066-200', 'ECE 2066-201', 'ECE 2066-202', 'ECE 2066-203', 'ECE 2066-204', 'ECE 2066-205', 'ECE 2066-206', 'ECE 2066-207', 'ECE 2330-100', 
#                'ECE 2330-101', 'ECE 2330-102', 'ECE 2330-103', 'ECE 2330-104', 'ECE 2330-105', 'ECE 2330-106', 'ECE 2330-107', 'ECE 2630-001', 'ECE 2660-001', 'ECE 3250-001', 
#                'ECE 3251-002', 'ECE 3251-003', 'ECE 3430-001', 'ECE 3750-001', 'ECE 4140-001', 'ECE 4155-003', 'ECE 4265-001', 'ECE 4265-002', 'ECE 4332-001', 'ECE 4434-001', 
#                'ECE 4435-001', 'ECE 4457-001', 'ECE 4502-004', 'ECE 4550-001', 'ECE 4550-002', 'ECE 4550-003', 'ECE 4550-006', 'ECE 4660-001', 'ECE 4750-001', 'ECE 4860-001', 
#                'ECE 5150-001', 'ECE 5260-001', 'ECE 5502-001', 'ECE 5502-002', 'ECE 5755-001', 'ECE 6140-001', 'ECE 6155-001', 'ECE 6261-001', 'ECE 6265-001', 'ECE 6265-002']


# ---- To Test ----
# Use print statements of the given functions:
#   "course_finder.instructor_lectures('department', 'instructor')"
#   "course_finder.compatible_classes('first_class', 'second_class', need_open_space = False)"

# Example:
print(course_finder.instructor_lectures('BIOL', 'David Kittlesen'))
print(course_finder.compatible_classes('ECE 2066-100', 'ECON 2010-100'))
