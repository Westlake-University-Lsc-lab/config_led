# config_led
A script repo to config led pulse generator, with Combine Ch1+Ch2 mode, fixed Ch2 apm and offset,
with 50 Hz trigger rate, external trigger signal synchronized with Ch2 or Ch1.

#### Installation

```
git clone git@github.com:Westlake-University-Lsc-lab/config_led.git

```

#### Requirement

```
pip install pyvisa

```

#### Run script and configuring

```
python configuration.py 50 1.8 0.9 5

```
the first parameter [50 Hz] is trigger rate, [1.8 V] is Ch1 Amp, [0.9 V] is offset,
[5 us] is the delay time length of Ch2 from Ch1. The external trigger signal synchronized
with Ch1 when delay time smaller or equal than 5 us, and synchronized with Ch2 when
delay time larger than 5 us.

#### Edit DAW_Config file
```
python write_config.py self
python write_config.py ext
python write_config.py ext 175 external_trigger_file_name
python write_config.py self 40 20 self_trigger_file_name

```

two trigger style options, external or self trigger.
external trigger command format
```
python write_config.py trig_style rec_len file_name

```
self trigger command format
```
python write_config.py trig_style rec_len threshold file_name

```