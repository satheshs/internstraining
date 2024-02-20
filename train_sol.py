import sys

trainA = [
    {"name": "CHN", "kms": 0},
    {"name": "SLM", "kms": 350},
    {"name": "BLR", "kms": 550},
    {"name": "KRN", "kms": 900},
    {"name": "HYB", "kms": 1200},
    {"name": "NGP", "kms": 1600},
    {"name": "ITJ", "kms": 1900},
    {"name": "BPL", "kms": 2000},
    {"name": "AGA", "kms": 2500},
    {"name": "NDL", "kms": 2700}
]

trainB = [
    {"name": "TVC", "kms": 0},
    {"name": "SRR", "kms": 300},
    {"name": "MAQ", "kms": 600},
    {"name": "MAO", "kms": 1000},
    {"name": "PNE", "kms": 1400},
    {"name": "HYB", "kms": 2000},
    {"name": "NGP", "kms": 2400},
    {"name": "ITJ", "kms": 2700},
    {"name": "BPL", "kms": 2800},
    {"name": "PTA", "kms": 3800},
    {"name": "NJP", "kms": 4200},
    {"name": "GHY", "kms": 4700}
]

# args = sys.argv[1:]

# TRAIN_A ENGINE NDL NDL KRN GHY SLM NJP NGP BLR
# TRAIN_B ENGINE NJP GHY AGA PNE MAO BPL PTA
inputA = "TRAIN_A ENGINE NDL NDL KRN GHY SLM NJP NGP BLR"
inputB = "TRAIN_B ENGINE NJP GHY AGA PNE MAO BPL PTA"

trainAInput = [i.replace("TRAIN_A", "").replace("ENGINE", "") for i in inputA.split() if i]
trainBInput = [i.replace("TRAIN_B", "").replace("ENGINE", "") for i in inputB.split() if i]

trainAHyd = next(station for station in trainA if station["name"] == "HYB")
trainBHyd = next(station for station in trainB if station["name"] == "HYB")

def collect_stations(train_input):
    stations = []
    for data in train_input:
        stationFoundTrainA = next((station for station in trainA if station["name"] == data), None)
        stationFoundTrainB = next((station for station in trainB if station["name"] == data), None)
        if stationFoundTrainA and stationFoundTrainA["kms"] >= trainAHyd["kms"]:
            stations.append({"station": stationFoundTrainA["name"], "kms": stationFoundTrainA["kms"]})
        elif stationFoundTrainB and stationFoundTrainB["kms"] >= trainBHyd["kms"]:
            stations.append({"station": stationFoundTrainB["name"], "kms": stationFoundTrainB["kms"]})
    return stations

stationsA = collect_stations(trainAInput)
stationsB = collect_stations(trainBInput)


departure = sorted(stationsA + stationsB, key=lambda x: x["kms"], reverse=True)
departure = [d for d in departure if d["station"] != "HYB"]

if len(stationsA):
    TrainAoutput = "ARRIVAL TRAIN_A ENGINE "
else:
    TrainAoutput = "JOURNEY_ENDED"
    
if len(stationsB):
    TrainBoutput = "ARRIVAL TRAIN_B ENGINE "
else:
    TrainBoutput = "JOURNEY_ENDED"

if departure:
    TrainABoutput = "DEPARTURE TRAIN_AB ENGINE ENGINE "
else:
    TrainABoutput = "JOURNEY_ENDED"

print(TrainAoutput + " ".join(data["station"] for data in stationsA))
print(TrainBoutput + " ".join(data["station"] for data in stationsB))
print(TrainABoutput + " ".join(data["station"] for data in departure))