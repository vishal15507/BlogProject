from flask import Flask, render_template, url_for, request
from all_posts import all_posts
app = Flask(__name__)



@app.route('/')
def home():
    posts = all_posts
    print(posts)
    return render_template("body.html",name="index.html",all_posts=posts)

@app.route("/about")
def about_us():
    return render_template("body.html",name="about.html")

@app.route("/contact")
def contact_us():
    return render_template("body.html",name="contact.html")

@app.route("/details",methods=["POST"])
def send_email():
    if request.form["name"] and request.form["email"] and request.form["phone"] and request.form["message"]:
        name=request.form["name"]
        email=request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        import smtplib
        MY_EMAIL = "vishaldemothool@gmail.com"
        MY_PASSWORD = "L2H2qFpjmJn!LcP"
        details=f'''
                    Name:{name}
                    email:{email}
                    phone:{phone}
                    message:{message}'''
        with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="vishalthool15507@gmail.com"
                                , msg=f"Subject: Details Of The Visitor\n\n{details}")

        return f'<a href="/">Message sent successful</a>'
    else:
        return "Please enter valid credentials"

@app.route("/post/<int:index>")
def each_post(index):
    for blog_post in all_posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("body.html",name="post.html",post=requested_post)



if __name__ == "__main__":
    app.run(debug=True,host="localhost",port=5000)