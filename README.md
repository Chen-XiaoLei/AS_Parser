# AS_Parser
This repository contains the code and the main data used for the experiments in the paper titled "AS-Parser: Log Parsing Based on Adaptive Segmentation" by [XiaoLei Chen, Peng Wang, Jia Chen, Wei Wang]. The purpose of this README is to provide detailed instructions on how to run the code.

The folder `benchmark` contains the code for running experiments on 16 benchmark datasets. You can obtain the results for these 16 benchmark datasets by running the `ASParser_benchmark.py` file.

The folder `logparser` contains the code for ASParser.

The folder `logs` contains 16 benchmark dataset from loghub (https://github.com/logpai/loghub)

The folder `result` is the output path in `benchmark/ASParser_benchmark.py`

The code is written in Python, and we recommend using Python 3.9 or higher. You can run
```bash
pip install -r requirements.txt
```
to set up the environment.

`main.py` is a demo that uses ASParser. Four parameters are needed:
1. `log_format` is the format of log header and log message. If you don't want to remove the log header, just set log_format="<Content>"
2. `indir` is the path of your dataset.
3. `outdir` is the path you wish to output the results.
4. `st` is the threshold.

If you want to load log files in other format, please rewrite the function `log_to_dataframe` in `logparser/ASParser/ASParser.py`
