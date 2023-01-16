# SPDX-FileCopyrightText: Copyright (c) 2022 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: MIT

from .ctc import set_decoder_num_classes
from .ctc_bpe import bpe_check_inputs_and_version
from .mtencdec import change_tokenizer_names
from .tts import fastpitch_model_versioning, generate_vocab_mapping, radtts_model_versioning

patches = {
    "EncDecCTCModel": [set_decoder_num_classes],
    "EncDecCTCModelBPE": [bpe_check_inputs_and_version],
    "MTEncDecModel": [change_tokenizer_names],
    "FastPitchModel": [generate_vocab_mapping, fastpitch_model_versioning],
    "RadTTSModel": [generate_vocab_mapping, radtts_model_versioning],
}