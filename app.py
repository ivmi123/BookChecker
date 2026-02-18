import streamlit as st

# ---------- INITIAL BOOK DATABASE ----------
if "books" not in st.session_state:
    st.session_state.books = [
        {"title": "The Hobbit", "author": "J.R.R. Tolkien"},
        {"title": "1984", "author": "George Orwell"},
        {"title": "Pride and Prejudice", "author": "Jane Austen"},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    ]

# ---------- APP TITLE ----------
st.title("📚 Book Manager & Checker App")

st.write("Add new books or check if a book exists in the database.")

# ==================================================
# ADD BOOK SECTION
# ==================================================

st.subheader("➕ Add a New Book")

title = st.text_input("Title")
author = st.text_input("Author")

if st.button("Add Book"):
    if title.strip() == "" or author.strip() == "":
        st.warning("Please enter both title and author.")
    else:
        new_book = {"title": title.strip(), "author": author.strip()}
        st.session_state.books.append(new_book)
        st.success("Book added successfully!")

# ==================================================
# CHECK BOOK SECTION
# ==================================================

st.subheader("🔍 Check if a Book Exists")

check_title = st.text_input("Enter book title to check")

if st.button("Check Book"):
    if check_title.strip() == "":
        st.warning("Please enter a book title.")
    else:
        exists = any(
            book["title"].lower() == check_title.strip().lower()
            for book in st.session_state.books
        )

        if exists:
            st.success("The book exists in the database!")
        else:
            st.error("The book is NOT in the database.")

# ==================================================
# DISPLAY ALL BOOKS
# ==================================================

st.subheader("📖 Book List")

for book in st.session_state.books:
    st.write(f"**{book['title']}** by {book['author']}")
