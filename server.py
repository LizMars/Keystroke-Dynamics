from bottle import run, request, post
import os
import json
import subprocess
import checkname
import profile
import auth

@post('/')
def index():

    postdata = request.json

    if postdata == 400:
        print "Error invaid JSON"

    else:
        user = request.get_header("User")
        typepost = request.get_header("Type")
        print user, typepost
        if typepost != "is_in_DB":
            postfile = typepost + "_" + user + "POST.json"
            with open(postfile, "w") as f:
                f.write(json.dumps(postdata))

        if " " in user:
            user.replace(" ", "_")


        if typepost == "Create_Profile":
            if profile.new_profile(postfile):
                print "Profile Created"
                return "True"
            else:
                print "Fail. Something gone wrong"
                return "False"
            #os.system("python profile.py " + postfile)

        elif typepost == "Auth":
            print "Auth begin for ", user
            return auth.start_auth(postfile)

            #os.system("python auth.py " + postfile)

        elif typepost == "is_in_DB":
            print "Checkname Status for", user, ": ",
            if checkname.is_record_exists(user):
                print "Alredy Exist"
                return "User Name Already Exist"
            else:
                print "New Name"
                return "OK"

        #return "Thank you. Your data processed and will ready to view soon."

if __name__ == "__main__":
    run(host='0.0.0.0', port=8080)
