from flask import Flask, jsonify, request
from flask_cors import CORS
from config import db, SECRET_KEY
from os import environ, path, getcwd
from dotenv import load_dotenv
from models.user import User
from models.personalDetails import PersonalDetails
from models.experiences import Experiences
from models.projects import Projects
from models.skills import Skills
from models.education import Education
from models.certificates import Certificates

load_dotenv(path.join(getcwd(), '.env'))

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = False
    app.secret_key = SECRET_KEY
    db.init_app(app)
    print("DB Initialized Sucessfully")

    CORS(app)

    with app.app_context():
        @app.route('/add_user', methods=['POST'])
        def add_user():
            data = request.form.to_dict(flat=True)
            print(data)
            new_user = User(
                username=data["username"]
            )
            db.session.add(new_user)
            db.session.commit()
            return jsonify(msg="User Added Successfully")

        @app.route('/add_personal_details', methods=['POST'])
        def add_personal_details():
            username = request.args.get('username')
            user = User.query.filter_by(username=username).first()
            print(username)
            personal_data = request.get_json()
            new_personal_details = PersonalDetails(
                name=personal_data["name"],
                phone=personal_data["phone"],
                email=personal_data["email"],
                address=personal_data["address"],
                linkedin_link=personal_data["linkedin_link"],
                user_id=user.id
            )
            db.session.add(new_personal_details)
            db.session.commit()
            print(personal_data)
            return jsonify(msg="Personal Details Added Successfully")

        @app.route('/add_projects', methods=['POST'])
        def add_project():
            username = request.args.get('username')
            user = User.query.filter_by(username=username).first()
            project_data = request.get_json()
            for data in project_data["data"]:
                new_project = Projects(
                    name=data["name"],
                    desc=data["description"],
                    start_date=data["start_date"],
                    end_date=data["end_date"],
                    user_id=user.id
                )
                db.session.add(new_project)
            db.session.commit()
            return jsonify(msg="Project Added Successfully")

        @app.route('/add_experiences', methods=['POST'])
        def add_experiences():
            username = request.args.get('username')
            user = User.query.filter_by(username=username).first()
            experience_data = request.get_json()
            print(experience_data)
            for data in experience_data["data"]:
                new_experience = Experiences(
                    company_name=data["company_name"],
                    role=data["role"],
                    role_desc=data["role_desc"],
                    start_date=data["start_date"],
                    end_date=data["end_date"],
                    user_id=user.id
                )
                db.session.add(new_experience)
            db.session.commit()
            return jsonify(msg="Experiences Added Successfully")

        @app.route('/add_education', methods=['POST'])
        def add_education():
            username = request.args.get('username')
            user = User.query.filter_by(username=username).first()
            education_data = request.get_json()
            print(education_data)
            for data in education_data["data"]:
                new_education = Education(
                    school_name=data["school_name"],
                    degree_name=data["degree_name"],
                    start_date=data["start_date"],
                    end_date=data["end_date"],
                    user_id=user.id
                )
                db.session.add(new_education)
            db.session.commit()
            return jsonify(msg="Education Added Successfully")

        @app.route('/add_skills', methods=['POST'])
        def add_skills():
            username = request.args.get('username')
            user = User.query.filter_by(username=username).first()
            skills_data = request.get_json()
            print(skills_data)
            for data in skills_data["data"]:
                new_skill = Skills(
                    name=data["name"],
                    confidence=data["confidence"],
                    user_id=user.id
                )
                db.session.add(new_skill)
            db.session.commit()
            return jsonify(msg="Skills Added Successfully")

        @app.route('/add_certificates', methods=['POST'])
        def add_certificates():
            username = request.args.get('username')
            user = User.query.filter_by(username=username).first()
            certificates_data = request.get_json()
            print(certificates_data)
            for data in certificates_data["data"]:
                new_certificate = Certificates(
                    title=data["title"],
                    start_date=data["start_date"],
                    end_date=data["end_date"],
                    user_id=user.id
                )
                db.session.add(new_certificate)
            db.session.commit()

            return jsonify(msg="Certificates Added Successfully")


        # @app.route('/get_resume', methods=['GET'])
        # def get_resume():
        #     username = request.args.get('username')
        #     user = User.query.filter_by(username=username).first()
        #     personal_details = PersonalDetails.query.filter_by(user_id=user.id).first()
        #     experiences = Experiences.query.filter_by(user_id=user.id).all()
        #     educations = Education.query.filter_by(user_id=user.id).all()
        #     projects = Projects.query.filter_by(user_id=user.id).all()
        #     certificates = Certificates.query.filter_by(user_id=user.id).all()
        #     skills = Skills.query.filter_by(user_id=user.id).all()

        #     experiences_data = []
        #     educations_data = []
        #     projects_data = []
        #     certificates_data = []
        #     skills_data = []

        #     resume_data = {
        #         "name": personal_details.name,
        #         "email": personal_details.email,
        #         "phone": personal_details.phone,
        #         "address": personal_details.address,
        #         "linkedin_link": personal_details.linkedin_link
        #     }

        #     # add experience
        #     for exp in experiences:
        #         experiences_data.append({
        #             "company_name": exp.company_name,
        #             "role": exp.role,
        #             "role_desc": exp.role_desc,
        #             "start_date": exp.start_date,
        #             "end_date": exp.end_date
        #         })
        #     resume_data["experiences"] = experiences_data

        #     # add projects
        #     for proj in projects:
        #         projects_data.append({
        #             "name": proj.name,
        #             "desc": proj.desc,
        #             "start_date": proj.start_date,
        #             "end_date": proj.end_date
        #         })

        #     resume_data["projects"] = projects_data

        #     return resume_data


        @app.route('/get_resume_json', methods=['GET'])
        def get_resume_json():
            username = request.args.get('username')
            user = User.query.filter_by(username=username).first()
            personalDetails = PersonalDetails.query.filter_by(user_id=user.id).first()
            experiences = Experiences.query.filter_by(user_id=user.id).all()
            educations = Education.query.filter_by(user_id=user.id).all()
            skills = Skills.query.filter_by(user_id=user.id).all()
            certificates = Certificates.query.filter_by(user_id=user.id).all()
            projects = Projects.query.filter_by(user_id=user.id).all()

            projects_data = []
            experiences_data = []
            educations_data = []
            certificates_data = []
            skills_data = []

            resume_data = {
                "personalDetails": {
                    "name": personalDetails.name,
                    "email": personalDetails.email,
                    "phone": personalDetails.phone,
                    "address": personalDetails.address,
                    "linkedin_url": personalDetails.linkedin_link
                }
            }
            
            #add experience data
            for exp in experiences:
                data = {
                    "company_name": exp.company_name,
                    "role_name": exp.role,
                    "role_description": exp.role_desc,
                    "start_date": exp.start_date,
                    "end_date": exp.end_date
                }
                experiences_data.append(data)
            resume_data["experiences"] = experiences_data

            for edu in educations:
                data = {
                    "school_name": edu.school_name,
                    "degree_name": edu.degree_name,
                    "start_date": edu.start_date,
                    "end_date": edu.end_date
                }
                educations_data.append(data)
            resume_data["educations"] = educations_data

            for skill in skills:
                data = {
                    "skill_name": skill.name,
                    "confidence_score": skill.confidence
                }
                skills_data.append(data)
            resume_data["skills"] = skills_data

            for cert in certificates:
                data = {
                    "title": cert.title,
                    "start_date": cert.start_date,
                    "end_date": cert.end_date
                }
                certificates_data.append(data)
            resume_data["certificates"] = certificates_data

            for project in projects:
                data = {
                    "project_name": project.name,
                    "project_description": project.desc,
                    "start_date": project.start_date,
                    "end_date": project.end_date
                }
                projects_data.append(data)
            resume_data["projects"] = projects_data

            return jsonify(resume_data)

        # db.drop_all()
        db.create_all()
        db.session.commit()
        return app



if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port='4545', debug=True)