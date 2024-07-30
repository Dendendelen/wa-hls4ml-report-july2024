wa-hls4ml GNN for July 2024 report.

Recent advancements in use of machine learning (ML) techniques on field-programmable gate arrays
(FPGAs) have allowed for the implementation of embedded neural networks with extremely low latency.
This is invaluable for particle detectors at the Large Hadron Collider, where latency and used area
are strictly bounded. The hls4ml framework is a procedure that converts trained ML model software
to a synthesis result to can be used on an FPGA. However, running the pipeline is a time-consuming
procedure, and there is a strong risk of failure. In particular, it may not be possible to successfully convert
a model into a synthesis result, or the resource consumption of the model may exceed the resources of
the target FPGA. To aid with this development, we introduce wa-hls4ml, a surrogate model using a
graph neural network to emulate the structure of the source models. The goal is to estimate the chance
of success and resource consumption of a given model when passed through the hls4ml pipeline, without
needing to run the pipeline.

Code used for this analysis is linked from this repository.
