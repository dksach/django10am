from django.shortcuts import render

# Create your views here.

def index(request):
    data =[
    "Alice", "Bob", "Charlie", "David", "Emma",
    "Frank", "Grace", "Henry", "Isabella", "Jack",
    "Katherine", "Liam", "Mia", "Noah", "Olivia",
    "Penelope", "Quinn", "Ryan", "Sophia", "Thomas",
    "Uma", "Victoria", "William", "Xander", "Yara",
    "Zoe", "Ava", "Benjamin", "Chloe", "Daniel",
    "Ella", "Finn", "Gabriella", "Hannah", "Isaac",
    "Jasmine", "Kai", "Lily", "Matthew", "Nora",
    "Owen", "Piper", "Quincy", "Riley", "Samuel",
    "Tessa", "Ulysses", "Violet", "Wyatt", "Xenia",
    "Yasmine", "Zachary", "Amelia", "Bryce", "Cora",
    "Dylan", "Elise", "Felix", "Gemma", "Hayden",
    "Ivy", "Jacob", "Kylie", "Leo", "Maya",
    "Nathan", "Olive", "Parker", "Quincy", "Ruby",
    "Sebastian", "Taylor", "Uriel", "Valentina",
    "Wesley", "Ximena", "Yael", "Zara", "Alexander",
    "Bella", "Caleb", "Daisy", "Ethan", "Fiona",
    "Gavin", "Harper", "Ian", "Julia", "Kevin",
    "Leah", "Mason", "Natalie", "Oscar", "Paige",
    "Quinn", "Ronan", "Stella", "Theo", "Una",
    "Vivian", "Wyatt", "Xander", "Yara", "Zoe"
]
    return render(request,'index.html',context={'users':data})


def contact(request):
    data = [
    "123-456-7890", "987-654-3210", "555-123-4567",  # ... and so on for other contact numbers
    ]

    return render(request,'contact.html',context={'users':data})

def address(request):
    data = [
    "123 Main St, City, State", "456 Elm St, City, State", "789 Oak St, City, State",  # ... and so on for other addresses
    ]   
    return render(request,'address.html',context={'users':data})

def insert(request):
    return render(request,"insert.html")



