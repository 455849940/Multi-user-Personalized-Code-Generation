from typing import List, Optional

from dataclasses import dataclass, field
from transformers import TrainingArguments

@dataclass
class train_config(TrainingArguments):
    
    human_eval: bool = field(
        default= False,
        metadata={"help": "human_eval"}
    )
    human_uid: int = field(
        default= -1,
        metadata={"help": "human_uid"}
    )
    human_prompt_uid: int = field(
        default= 3,
        metadata={"help": "human_uid"}
    )
    human_eval_out_path: str = field(
        default="./out_predict/",
        metadata={"help": "humaneval_java datasets paths."}
    )
    
    continue_train: str = field(
        default= False,
        metadata={"help": "continue train."}
    )
    choose_model_name: str = field(
        default="perfer_Base", 
        metadata={"help": "perfer_Base perfer_Aug perfer_AugT"}
    )
    
    scaler: bool = field(
        default= True,
        metadata={"help": "scaler"}
    )
    
    # model params
    alpha : float = field(
        default=0.1,
        metadata={"help": "alpha for loss"}
    )
    gradient_accumulation_steps: int = field(
        default = 1,
        metadata={"help": "gradient_accumulation_steps"}
    )
    enable_contrast:  bool = field(
        default= False,
        metadata={"help": "enable_contrast."}
    )
    enable_fsdp: bool = field(
        default= True,
        metadata={"help": "enable_fsdp."}
    )
    hidden_size: int = field(
        default=4096,
        metadata={"help": "coadellam-7b config.json hidden_size."}
    )
    
    vocab_size: int = field(
        default=32016,
        metadata={"help": "coadellam-7b config.json vocab_size."}
    )
    
    freezeLM: bool = field(
        default= True,
        metadata={"help": "freeze LM params."}
    )
    
    save_model: bool = field(
        default= True,
        metadata={"help": "save_model."}
    )
    
    model_name_or_path: str = field(
        default="./CodeLlama-7b-Instruct-hf", 
        metadata={"help": "the path to load pretrained model."}
    )

    tokenizer_path: str = field(
        default="./CodeLlama-7b-Instruct-hf", 
        metadata={"help": "the path to load pretrained tokenizer."}
    )
    pooling_type: str = field(
        default="average",
        metadata={"help": "the pooling method for reward model, selected from [average, max, last]."}
    )

    best_epoch: int = field(
        default=0,
        metadata={"help": "eval best epoch."}
    ) 
    # mode generate
    
    temperature: float = field( default=0.0, metadata={"help": "generate temperature"})
    top_p: float = field( default=0.9, metadata={"help": "generate top_p"})
    max_total_seq_len: int = field(default=3000,metadata={"help": "generate_length."})
    max_generate_length: int = field(default=1000,metadata={"help": "generate_length."})  
    # experiment setups
    
    output_dir: str = field(
        default="part_model", 
        metadata={"help": "output_dir"}
    )
    
    predict_dirs: str = field(
        default="./out_predict/result_part.json", 
        metadata={"help": "predict_dirs"}
    )
    
    # tokenizer params
    padding_side: str = field(
        default="right",
        metadata={"help": "the direction for tokenizer to add padding tokens."}
    )

    per_device_test_batch_size: int = field(default= 2,metadata={"help": "per_device_test_batch_size."})

    # data params
    language : str = field(default="Java",metadata={"help": "language data."})   
    problem_path: str = field(
        default="/home/develop/dzl/PreferCodeLlama/data/content_compelete.json",
        metadata={"help": "the path to load data."}
    )   
    human_eval_path: str = field(
        default="./data/humaneval_java.jsonl",
        metadata={"help": "humaneval_java datasets paths."}
    )
    human_eval_out_path: str = field(
        default="./out_predict/humaneval_java_out.jsonl",
        metadata={"help": "humaneval_java datasets paths."}
    )
    train_data_path: List[str] = field(
        default_factory=lambda: ["./data/Java_programming/Java_programming_train.json"],
        metadata={"help": "train datasets paths."}
    )

    eval_data_path: List[str] = field(
        default_factory=lambda: ["./data/Java_programming/Java_programming_dev.json"],
        metadata={"help": "evaluation datasets paths."}
    )

    test_data_path: List[str] = field(
        default_factory=lambda: ["/home/develop/dzl/PreferCodeLlama/data/Java_programming/Java_programming_test.json"],
        metadata={"help": "train datasets paths."}
    )
    
    feature_train_data_path: List[str] = field(
        default_factory=lambda: ["./data/Java_programming/Java_feature/feature_train.json"],
        metadata={"help": "train datasets paths."}
    )
   
    
    # training hyperparams
    eval_at_start: bool = field(
        default=False,
        metadata={"help": "whether make eval at start."}
    )

    debug_mode: bool = field(
        default=False,
        metadata={"help": "whether use the debug mode."}
    )

    weight_decay: float = field(default=0.0, metadata={"help": "weight_decay"})
    
    lm_loss_coeff: float = field(default=0., metadata={"help": "the coefficient for language modeling loss."})

    contrast_loss_coeff: float = field(default=0., metadata={"help": "the coefficient for contrastive learning loss."})

    gamma: float = field(default=0.85, metadata={"help": "model gamma"})

    max_length: int = field(
        default=4096,
        metadata={"help": "the max sentence sequence length."}
    )   



    

