from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm

console = Console()
LIBRARY_FILE = "library.txt"

def load_library():
    library = []
    try:
        with open(LIBRARY_FILE, "r") as file:
            for line in file:
                title, author, year, genre, read = line.strip().split(" | ")
                library.append({
                    "title": title,
                    "author": author,
                    "year": int(year),
                    "genre": genre,
                    "read": read == "True"
                })
    except FileNotFoundError:
        pass
    return library

def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        for book in library:
            file.write(f"{book['title']} | {book['author']} | {book['year']} | {book['genre']} | {book['read']}\n")

def display_books(library):
    if not library:
        console.print("[bold red]No books in your library![/]")
        return
    
    table = Table(title="\n📚[bold blue] Your Personal Library")
    table.add_column("Title", style="cyan")
    table.add_column("Author", style="magenta")
    table.add_column("Year", justify="center")
    table.add_column("Genre", style="green")
    table.add_column("Read", justify="center")
    
    for book in library:
        table.add_row(book["title"], book["author"], str(book["year"]), book["genre"], "✅" if book["read"] else "❌")
    
    console.print(table)

def add_book(library):
    title = Prompt.ask("Enter the book title")
    author = Prompt.ask("Enter the author")
    year = Prompt.ask("Enter publication year", default="2024").strip()
    genre = Prompt.ask("Enter genre")
    read = Confirm.ask("Have you read this book?")
    
    book = {"title": title, "author": author, "year": int(year), "genre": genre, "read": read}
    library.append(book)
    save_library(library)
    console.print(f"[bold green]'{title}' added to your library![/]")

def remove_book(library):
    title = Prompt.ask("Enter the title of the book to remove")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library(library)
            console.print(f"[bold red]'{title}' removed from your library![/]")
            return
    console.print("[bold yellow]Book not found![/]")

def search_book(library):
    search_term = Prompt.ask("Enter a title or author to search for")
    results = [book for book in library if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower()]
    
    if results:
        display_books(results)
    else:
        console.print("[bold yellow]No matching books found.[/]")

def display_stats(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    read_percentage = (read_books / total_books * 100) if total_books > 0 else 0
    console.print(f"[bold]Total Books:[/] {total_books}")
    console.print(f"[bold]Books Read:[/] {read_books} ({read_percentage:.2f}%)")

def filter_by_genre(library):
    genre = Prompt.ask("Enter genre to filter by")
    filtered_books = [book for book in library if book["genre"].lower() == genre.lower()]
    display_books(filtered_books) if filtered_books else console.print("[bold yellow]No books found in this genre.[/]")

def main():
    library = load_library()
    
    while True:
        console.print("\n[bold blue]📖 Personal Library Manager[/]\n")
        console.print("1. Add a book\n2. Remove a book\n3. Search for a book\n4. Display all books\n5. Display statistics\n6. Filter by Genre\n7. Exit")
        
        choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "4", "5", "6", "7"])
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_stats(library)
        elif choice == "6":
            filter_by_genre(library)
        elif choice == "7":
            console.print("[bold green]Library saved. Goodbye![/]")
            break

if __name__ == "__main__":
    main()
