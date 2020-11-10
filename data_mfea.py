class DataMFEA: 
    """
    Data returned from MFEA
    """
    def __init__(self, EvBestFitness, bestInd_data):
        self.EvBestFitness = EvBestFitness
        self.bestInd_data = bestInd_data