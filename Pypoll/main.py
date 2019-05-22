import pandas as pd

election_data=pd.read_csv("election_data.csv")


total_votes=len(election_data["Voter ID"])

 def function(Candidate="Khan"):
     candidate_total=len(election_data[election_data["Candidate"]==Candidate])
     candidate_percentage=round(((len(election_data[election_data["Candidate"]==Candidate]))/total_votes)*100,3)
     print(f"{Candidate}: {candidate_percentage} ({candidate_total})")
     return
Winner=max(election_data["Candidate"][election_data["Candidate"].value_counts()])


print=("Election Results")
print=("______________________")
print=(f"Total Votes:{total_votes}")
print=("______________________")
function("Khan")
function("Correy")
function("Li")
function("O'Tooley")
print=(f"Winner: {Winner}")

