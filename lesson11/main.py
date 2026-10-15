import app.users as us
import app.statistics as st

us.add_user("Ayxan", 24, "aykhan@gmail.com")
us.add_user("Tural", 19, "tural@gmail.com")
us.add_user("A", -19, "aykhan.com")


us.show_users()
print(st.get_count_users(us.users))
print(us.find_user_by_email("tural@gmail.com"))