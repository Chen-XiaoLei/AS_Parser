from logparser import ASParser



log_format = "<Date> <Time> <Pid> <Level> <Component>: <Content>"

indir = "logs/HDFS/"

outdir = "result/"

st = 0.75

parser = ASParser.LogParser(log_format=log_format, indir=indir,
                             outdir=outdir,st=st)

parser.parse("HDFS_2k.log")