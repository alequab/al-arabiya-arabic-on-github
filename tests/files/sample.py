# تعليق عربي: هذه الدالة تحيي المستخدم
def greet(name):
    # Comment in English, then عربي in the middle
    message = "مرحبًا يا " + name  # نص عربي داخل سلسلة
    print(message)  # print بالعربية
    return "GitHub: " + message


greet("أحمد")
