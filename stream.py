import pandas as pd

# Read the CSV file into a DataFrame
data = pd.read_csv('machineLearning.csv')

# for e in data.iterrows():
#     print(e[1])
#     print("@@@@@@@@@@@@@@@@@@@@@@@")


# Function to generate the HTML table rows dynamically
def generate_table_rows():
    rows = ''
    for _, row in data.iterrows():
        row_html = f"""
            <tr>
                <td>{row[0]}</td>
                <td>{row[1]}</td>
            </tr>
        """
        rows += row_html
    return rows


# Read the HTML template file and replace placeholders with the dynamic table rows
with open('template.html', 'r', encoding="utf-8") as file:
    template = file.read()

template = template.replace('REPLACE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', generate_table_rows())
# print(updated_html)

# Save the updated HTML to a new file
with open('myJob.html', 'w', encoding="utf-8") as file:
    file.write(template)
