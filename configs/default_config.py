#Default Config Value Section

class DefaultExperimentValues:
    DEFAULT_HPC = True

    DEFAULT_PROJECT_NAME= "Connectivity_Distillation_Experiment"
    DEFAULT_MODE = None
    DEFAULT_REPEAT_EXPERIMENT = 1
    DEFAULT_AE_LATENT_DIM = 32
    DEFAULT_AE_MAX_EPOCH = 100
    DEFAULT_AE_MODEL_PATH =  ""#Connectivity_Distillation_Experiment/nhxncpji/checkpoints/best_model.ckpt"
    DEFAULT_CLASSIFIER_MAX_EPOCH = 70
    DEFAULT_NUM_CLASSES = 8
    TOPO_LOSS_FN_NAME = ""
   
    DEFAULT_CLASSIFIER_LR = 0.0001
    DEFAULT_CLASSIFIER_WIEGHT_DECAY = 0.00001
    
    DEFAULT_AE_LR = 0.0001
    DEFAULT_BETA = 0.0
    DEFAULT_TOPO_WEIGHT = 0.0
    DEFAULT_DISTANCE_FN_NAME = 'euclidean'
    DEFAULT_DISTILLATION_LOSS_NAME = ''
    DEFAULT_DISTILLATION_LOSS_CONFIG = {}
    DEFAULT_AE_WIEGHT_DECAY = 0.0000005
