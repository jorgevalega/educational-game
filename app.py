from flask import Flask, render_template, request

app = Flask(__name__)

# Uppercase and lowercase letters (A-Z, a-z)
uppercase_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
lowercase_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
letters = uppercase_letters + lowercase_letters

# Group letters: 13 per page
letters_per_page = 13
letter_pages = [letters[i:i + letters_per_page] for i in range(0, len(letters), letters_per_page)]

# Numbers from 0 to 100
numbers = [str(i) for i in range(101)]

# First group: 0 to 10 (11 numbers), then groups of 10
number_pages = [numbers[0:11]] + [numbers[i:i + 10] for i in range(11, 101, 10)]

# Total pages
total_letter_pages = len(letter_pages)
total_number_pages = len(number_pages)
total_pages = total_letter_pages + total_number_pages

@app.route("/")
def index():
    """
    Main route of the application.
    Renders the page with the current group of letters or numbers.
    """
    page = int(request.args.get("page", 1))

    # Fix invalid page numbers
    if page < 1 or page > total_pages:
        page = 1

    if page <= total_letter_pages:
        group = letter_pages[page - 1]
        content_type = "Letters"
        current_page = page
        total = total_letter_pages
    else:
        index_number = page - total_letter_pages - 1
        group = number_pages[index_number]
        content_type = "Numbers"
        current_page = index_number + 1
        total = total_number_pages

    return render_template(
        "index.html",
        group=group,
        page=page,
        total=total_pages,
        type=content_type,
        pagina_atual=current_page,
        paginas_total=total
    )

if __name__ == "__main__":
    app.run(debug=True)
