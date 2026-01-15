pipeline{
    agent any

    stages{
        stage('stage one get code'){

            steps{
                git branch : 'main' ,
                url : 'https://github.com/gauriNimbalkar/PythonFormPipeline.git'
                
            }
    }

         stage('stage two check python'){

            steps{
                bat"""python --version"""
            }
         }
         
         stage('stage three for installation'){

            steps{

                bat""" pip install -r requirements.txt """
            }
         }

         stage('stage four run project'){

            steps{
                bat""" python app.py """
            }
         }
    

    }
}