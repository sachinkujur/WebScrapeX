import PyPDF2
import datetime


def open_protected_pdf(pdf_path, password_prefix):
    try:
        pdf_file = open(pdf_path, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Generate possible passwords by combining with all day-month combinations
        today = datetime.datetime.now()
        current_year = today.year

        for month in range(1, 13):  # Loop through months
            for day in range(1, 32):  # Loop through days
                try:
                    possible_password = password_prefix + f"{day:02d}{month:02d}"

                    if pdf_reader.decrypt(possible_password):
                        num_pages = len(pdf_reader.pages)
                        print(f"PDF has {num_pages} pages.")

                        for page_num in range(num_pages):
                            page = pdf_reader.pages[page_num]
                            print(f"Page {page_num + 1}:\n")
                            print(page.extract_text())

                        pdf_file.close()
                        return  # Exit if correct password found

                except Exception as e:
                    pass  # Incorrect password, continue to next combination

        print("Password not found.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        pdf_file.close()


if __name__ == "__main__":
    pdf_path = r"C:\Users\user\Downloads\00476067-XXXXXXXXX160XXX9705-560034-25072023.pdf"
    password_prefix = input("Enter the first 4 letters of the password: ")
    open_protected_pdf(pdf_path, password_prefix)
