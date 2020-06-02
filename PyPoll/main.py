
import csv
import os


#get relative file path

csv_path = os.path.join("Resources", "election_data.csv")


#initialize two list to pick up the canadiates and total votes for each

candidates = []
votes = []

with open (csv_path, "r", newline="", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    headers = next(csv_reader)

    # loop through each line, add uniqe candates to list and add 1 to votes everytime canadate appers

    for row in csv_reader:
        if row[2] in candidates:
            index_number = candidates.index(row[2])
            votes[index_number] = votes[index_number] + 1
        else:
            candidates.append(row[2])
            votes.append(1)
            

total_votes = sum(votes)



#loop throug every index in votes list and calculate % of votes and add to new list

votes_percentage = []

for index in votes:
    percentage = "{:.3f}" .format((index/total_votes)*100)
    votes_percentage.append(percentage)

winner = candidates[votes_percentage.index(max(votes_percentage))]


# create text output file to store the resluts of the analysis 

output_path = os.path.join("Analysis", "results.txt")

with open (output_path, "w", newline= "") as csv_output_file:
    csv_writer = csv.writer (csv_output_file, delimiter= ",")

    csv_writer.writerow(["Election Results"])
    csv_writer.writerow(["Total votes: " + str(total_votes)])


    for i in range (len(candidates)):
        csv_writer.writerow([f'{candidates[i]}: {votes_percentage[i]}% ({votes[i]})'])

    csv_writer.writerow(["winner: " + str(winner)])



# print the results


print("Election Results")
print("Total votes: " + str(total_votes))
for i in range (len(candidates)):
        print(f'{candidates[i]}: {votes_percentage[i]}% ({votes[i]})')
print("winner: " + str(winner))

