from crewai_trip_planning.crew import CrewaiTripPlanning

place = input("Enter the place: ")
trip_duration = input("Enter the trip duration: ")

def run():
    inputs = {
        "place": place,
        "trip_duration": trip_duration
    }

    print("Running with inputs:", inputs)
    CrewaiTripPlanning().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()
