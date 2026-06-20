import re

file_path = r'C:\Users\Gabriel\Desktop\anthropic_articles\llm-papers-kr\mathematical_framework.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Pattern 1
p1 = r'잔차 스트림\(Residual Stream\)은 고차원 벡터 공간이다\. 작은 모델에서는 수백 개의 차원일 수 있습니다; 대형 모델에서는 수만 명에 달할 수 있습니다\. 즉, 레이어는 서로 다른 부분공간에 저장함으로써 서로 다른 레이어로 다른 정보를 보낼 수 있습니다\. 특히 어텐션 헤드의 경우에는 모든 개별 머리가 비교적 작은 부분공간\(보통 64차원 또는 128차원\)에서 작동하며, 완전히 서로가 아닌 부분공간에 쉽게 쓰고 상호작용하지 않을 수 있기 때문입니다\.'
r1 = r'잔차 스트림(Residual Stream)은 고차원 벡터 공간입니다. 작은 모델의 경우 수백 차원에 불과할 수 있지만, 대형 모델에서는 수만 차원에 달하기도 합니다. 이는 곧 여러 계층(Layer)이 서로 다른 정보들을 각각의 독립된 부분 공간(subspace)에 저장함으로써 다른 계층으로 정보를 전송할 수 있음을 의미합니다. 특히 어텐션 헤드의 경우 이러한 특징이 두드러지는데, 개별 헤드는 비교적 작은 부분 공간(일반적으로 64차원 또는 128차원)에서만 연산을 수행하므로, 서로 겹치지 않는(disjoint) 부분 공간에 정보를 쓰고 상호작용을 피하는 것이 매우 쉽기 때문입니다.'
text = re.sub(p1, r1, text, flags=re.DOTALL)

# Pattern 2a
p2a = r'한 번 추가되면 다른 계층이 적극적으로 삭제하지 않는 한 서브스페이스에 정보가 유지됩니다\. 이 관점에서 잔차 스트림\(Residual Stream\)의 차원은 "메모리" 또는 "대역폭" 같은 것이 됩니다\. 원래 토큰 임베딩과 비임베딩은 대부분 비교적 작은 부분의 dimension과 상호작용합니다\.'
r2a = r'일단 정보가 추가되면 다른 계층이 이를 의도적으로 삭제하지 않는 이상 잔차 스트림(Residual Stream) 내에 계속 유지됩니다. 이런 관점에서 볼 때, 잔차 스트림(Residual Stream)의 차원은 \'메모리\' 또는 \'대역폭\'과 같은 역할을 한다고 볼 수 있습니다. 초기 토큰 임베딩(Token Embedding)과 언임베딩(Unembedding)은 대부분 비교적 적은 비율의 차원만을 사용합니다.'
text = re.sub(p2a, r2a, text, flags=re.DOTALL)

# Pattern 2b
p2b = r'이로 인해 대부분의 차원은 다른 계층들이 정보를 저장할 수 있도록 "자유로운" 공간이 됩니다\.'
r2b = r'이로 인해 나머지 대부분의 차원은 다른 계층들이 정보를 저장할 수 있도록 \'여유(free)\' 공간으로 남게 됩니다.'
text = re.sub(p2b, r2b, text, flags=re.DOTALL)

# Pattern 3
p3 = r'잔차 스트림\(Residual Stream\) 대역폭이 매우 수요가 많을 것으로 예상해야 할 것 같습니다! 일반적으로 잔차 스트림\(Residual Stream\)이 정보를 이동할 수 있는 차원보다 훨씬 더 많은 "계산 차원"\(예: 뉴런, 어텐션 헤드 결과 차원\)이 존재합니다\. 단일 MLP 층은 일반적으로 잔차 스트림\(Residual Stream\)의 차원보다 네 배 더 많은 뉴런을 가집니다\. 예를 들어, 50계층 트랜스포머 \(Zero-Layer Transformer\)의 25층에서, 잔차 스트림\(Residual Stream\)은 앞에 100배 더 많은 뉴런을 가지고 있어서, 그 뒤에 100배 더 많은 뉴런과 소통하려고 시도하며, 어떻게든 중첩 상태에서 소통하는 것입니다! 우리는 이렇게 텐서를 부릅니다 <a href="#def-bottleneck-activation">"병목 활성화"</a> 그리고 해석이 매우 어려울 것으로 예상해야 합니다\. \(이것이 우리가 잔차 스트림\(Residual Stream\)을 통해 일어나는 서로 다른 통신 흐름을 가상 가중치로 분리해 분석하려는 주요 이유 중 하나이며, 직접 연구하는 것이 아닙니다\.\)'
r3 = r'잔차 스트림(Residual Stream)의 대역폭은 수요가 매우 높을 수밖에 없습니다! 잔차 스트림(Residual Stream)이 정보를 전달하는 데 사용할 수 있는 차원 수에 비해, 연산을 담당하는 \'계산 차원\'(예: 뉴런 수, 어텐션 헤드 결과 차원)이 훨씬 더 많기 때문입니다. 단일 MLP 계층만 하더라도 일반적으로 잔차 스트림(Residual Stream) 차원 수의 4배에 달하는 뉴런을 가지고 있습니다. 예를 들어 50계층 트랜스포머의 25번째 계층을 생각해 보면, 잔차 스트림(Residual Stream)은 자신의 앞에 있는 100배 더 많은 뉴런과 그 뒤에 있는 100배 더 많은 뉴런 간의 통신을 중개해야 하며, 그 과정에서 어떤 식으로든 중첩(superposition) 상태로 정보를 주고받게 됩니다! 우리는 이러한 형태의 텐서를 <a href="#def-bottleneck-activation">\'병목 활성화(bottleneck activations)\'</a>라고 부르며, 이로 인해 모델의 내부를 해석하기가 극도로 어려워질 것이라고 예측할 수 있습니다. (이것이 우리가 잔차 스트림(Residual Stream)을 직접적으로 연구하는 대신, 가상 가중치(virtual weights)라는 개념을 도입하여 서로 다른 통신 흐름을 분리하고 분석하려는 주된 이유 중 하나입니다.)'
text = re.sub(p3, r3, text, flags=re.DOTALL)

# Pattern 4
p4 = r'잔차 스트림\(Residual Stream\) 대역폭에 대한 높은 수요 때문인지, 일부 MLP 뉴런과 어텐션 헤드가 일종의 \'메모리 관리\' 역할을 수행하는데, 다른 계층이 설정한 잔차 스트림\(Residual Stream\) 차원을 정보를 읽고 음의 값을 기록해 처리하는 것일 수 있다는 암시가 있습니다\.'
r4 = r'이러한 잔차 스트림(Residual Stream) 대역폭에 대한 높은 수요를 방증하듯, 일부 MLP 뉴런이나 어텐션 헤드가 일종의 \'메모리 관리(memory management)\' 역할을 수행한다는 단서들이 존재합니다. 즉, 다른 계층이 설정한 잔차 스트림(Residual Stream) 차원의 정보를 읽어들인 다음 그것의 음수(negative) 버전을 덮어씀으로써 해당 차원의 정보를 지워버리는(clearing out) 기능을 하는 것입니다.'
text = re.sub(p4, r4, text, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Replacement complete.")
