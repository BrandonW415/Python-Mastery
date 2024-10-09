
fruits = ['apple', 'banana', 'cherry', 'date']

fruits.append('elderberry')
fruits.remove('banana')
fruits.sort()

print(fruits)


student = {
    "name": "John Doe",
    "age": 25,
    "major": "Computer Science"
}

student["major"] = "Electrical Engineering"

student["year"] = "Senior"

print("Keys in the dictionary:")
print(student.keys())

print("\nValues in the dictionary:")
print(student.values())


books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}
]

print("Title of the second book:", books[1]["title"])
print("Year the third book was published:", books[2]["year"])
print("\nAll books:")
for book in books:
    print(f"Title: {book['title']}, Author: {book['author']}")
    
    
courses = {
    "math": ["Alice", "Bob", "Charlie", "Brandon"],
    "history": ["Eva", "Franklin", "Grace", "Henry", "Ivy"],
    "chemistry": ["Jack", "Katie", "Liam", "Mya", "Noah"]
}

courses["math"].extend(["Oliver", "Penny", "Quinn", "Rochelle", "Samantha"])

del courses["history"][2]

print("Students in chemistry:", courses["chemistry"])

courses["physics"] = ["Lamar", "Tiana", "Tyrell", "Xavier"]

print("\nFinal state of courses:")
for course, students in courses.items():
    print(f"{course}: {students}")