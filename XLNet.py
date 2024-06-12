from ...modeling_tf_utils import (
TFCausalLanguageModelingLoss,
    TFModelInputType,
    TFMultipleChoiceLoss,
    TFPreTrainedModel,
    TFQuestionAnsweringLoss,
    TFSequenceClassificationLoss,
    TFSequenceSummary,
    TFSharedEmbeddings,
    TFTokenClassificationLoss,
    get_initializer,
    keras,
    keras_serializable,
    unpack_inputs,
)

class TFXLNetPreTrainedModel(TFPreTrainedModel):
    """
    An abstract class to handle weights initialization and a
    simple interface for downloading and loading pretrained
    models.
    """
    config_class = XLNetConfig
    base_model_prefix = "transformer"
@dataclass

class TFXLNetModel(TFXLNetPreTrainedModel):
    def __init__(self, config, *inputs, **kwargs):
        super().__init__(config, *inputs, **kwargs)
        self.transformer = TFXLNetMainLayer(config, name="transformer")

    @unpack_inputs
    @add_start_docstrings_to_model_forward(XLNET_INPUTS_DOCSTRING.format("batch_size, sequence_length"))
    @add_code_sample_docstrings(
        checkpoint=_CHECKPOINT_FOR_DOC,
        output_type=TFXLNetModelOutput,
        config_class=_CONFIG_FOR_DOC,
    )
    
""""""""""
TFPreTrainedModel : 사전 학습된 모델을 다루는 클래스.
TFXLNetPreTrainedModel : TFPreTrainedModel을 상속받는 추상 클래스로,
사전 학습된 모델의 가중치 초기화 및 다운로드/로드함.
TFXLNetModel: TFXLNetPreTrainedModel을 상속받아 XLNet 모델의 주요 변환 층을 정의하고, 
모델의 문서화와 사용성을 개선하는 데코레이터를 포함하는 클래스.
""""""""""
