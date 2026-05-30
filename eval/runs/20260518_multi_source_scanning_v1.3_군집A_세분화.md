<!--
실사용 기록 (test record)
- 프롬프트: RES-001 다중 소스 스캐닝 v1.3
- 소스: 277개 소스 실행 결과 중 군집 A
- 실행 환경: NotebookLM
- 날짜: 2026-05-18
- 판정: partial
- 검증 포인트:
  - 과대 군집을 세부 연구 타겟 5개로 다시 나누는 데 성공.
  - 대규모 스캔 이후 후속 세분화가 유효함을 확인.
- 실패/한계:
  - 원 실행에서 바로 이 해상도까지 얻기는 어려움.
  - 군집별 후속 스캔을 별도 루틴으로 명시할 필요가 있음.
- 다음 수정:
  - RES-001 출력에 "후속 분할 권장 군집" 표시를 추가 검토한다.
-->

# 다중 소스 스캐닝 및 지형도 분석

**적용된 군집 기준**: 서지학(Bibliometric) 연구 문헌 내 세부 연구 타겟 (방문자 경험, 기후/탄소, 형평성, 설계 패러다임, 거시적 진화 궤적)

## 1. 지형도 개요 (Map Overview)
*과거 '군집 A'로 묶였던 서지학 및 체계적 문헌 고찰(Systematic Review) 연구들만 추출하여 스캐닝한 결과, 이들은 단순히 문헌의 총량을 세는 것을 넘어 명확한 세부 타겟을 향해 분화하고 있음을 알 수 있습니다. 이 문헌들은 크게 1) 소셜 미디어와 빅데이터를 활용한 '방문자 경험 및 만족도', 2) 탄소 격리 및 자연기반해법(NBS)에 집중하는 '기후 및 생태계 서비스', 3) 환경 정의와 소외 계층을 다루는 '사회적 형평성', 4) 하이라인 공원 모델이나 ROS 등 '설계 패러다임과 관리 프레임워크', 5) 지난 30년간의 흐름을 짚어내는 '거시적 진화 궤적'의 5가지 세부 지형으로 뚜렷하게 나뉩니다.*

## 2. 군집별 소스 분류 (Clusters)

### 군집 A: 방문자 경험, 만족도 및 충성도 동향 (Visitor Experience & Big Data) (약 3개)
- **공통된 뼈대/서사**: 전통적인 현장 조사를 넘어 빅데이터, 소셜 미디어 텍스트 마이닝 등을 활용해 공원 방문자의 행동, 만족도, 그리고 장소 애착(충성도)을 서지학적으로 추적하고 이를 공원 설계 최적화에 연결합니다.
- **대표 소스 (Top 3~5)**:
  - **"How Satisfaction Research Contributes to the Optimization of Urban Green Space Design..."**: 2001년부터 2024년까지의 문헌을 분석하여, 공원 사용자 만족도 연구가 생태적 기능, 거주자 요구, 관리 전략의 4가지 차원에서 어떻게 공원 설계를 최적화해왔는지 맵핑함 [1, 2].
  - **"A Systematic Review of Loyalty in Urban Green Spaces: Bibliometric Mapping and TCCM Analysis"**: 장소 애착, 만족도, 재방문 의도와 같은 '충성도' 관련 변인들이 어떻게 연결되는지 TCCM 프레임워크를 통해 서지학적으로 분석함 [3, 4].
  - **"A Literature Review of Big Data-Based Urban Park Research in Visitor Dimension"**: 위치 기반 소셜 미디어 등 빅데이터를 활용한 공원 방문객 연구의 시공간적 특징, 감성 분석(Sentiment Analysis) 기법 등을 정량적·정성적으로 종합함 [5, 6].

### 군집 B: 기후 복원력, 탄소 격리 및 생태계 서비스 동향 (Climate & Ecosystem Services) (약 3개)
- **공통된 뼈대/서사**: 도시공원의 역할을 탄소 흡수원, 수변-녹지(Blue-Green) 통합 인프라 등 기후 위기 대응 수단으로 정의하며, 생태계 서비스의 정량적 평가 연구들이 어떻게 발전해왔는지를 맵핑합니다.
- **대표 소스 (Top 3~5)**:
  - **"Progress of carbon sequestration in urban green space based on bibliometric analysis"**: 도시녹지의 탄소 격리(Carbon sequestration), 탄소 발자국, 기후 변화 등과 관련된 글로벌 연구 핫스팟과 기관 간 협력 네트워크를 분석함 [7, 8].
  - **"A bibliometric analysis on designing urban green and blue spaces related to environmental and public health benefits"**: 도시의 녹색(Green) 및 수청색(Blue) 공간의 설계가 환경적 가치와 공중 보건 혜택에 미치는 영향을 문헌 데이터를 통해 맵핑함 [9].
  - **"Bibliometric analysis of urban ecological spaces: research trajectories and future outlook"**: 도시 생태 공간(UES) 연구가 기초 생태학에서 다학제간 성장기를 거쳐 기술적 정교화 단계로 발전한 궤적을 제시함 [10].

### 군집 C: 사회적 형평성 및 공간적 접근성 동향 (Social Equity & Accessibility) (약 2개)
- **공통된 뼈대/서사**: 공원 녹지가 소득 수준, 인종, 연령 등에 따라 불균등하게 배분되는 환경 정의(Environmental Justice) 문제와 이를 해결하기 위한 정책적 담론의 진화 과정을 체계적 문헌 고찰로 분석합니다.
- **대표 소스 (Top 3~5)**:
  - **"Equity in park green spaces: a bibliometric analysis and systematic literature review from 2014-2023"**: 1차원적인 영토적 평등 개념에서 출발해 취약 계층의 요구를 반영하는 고차원적 사회 형평성으로 진화해 온 과정을 규명함 [11, 12].
  - **"Urban Green Space per Capita for Sustainable and Equitable Urban Planning: A Systematic Review and Bibliometric Analysis"**: 1인당 도시 녹지 면적(per Capita) 지표를 중심으로, 지속가능하고 공평한 도시 계획을 위한 학술적 접근의 한계와 발전 방향을 종합함 [13, 14].

### 군집 D: 공원 설계 패러다임 및 관리 프레임워크 동향 (Design Paradigm & Frameworks) (약 5개)
- **공통된 뼈대/서사**: 특정 설계 모델(예: 고가 철도를 재생한 하이라인)이나 공원 관리 프레임워크(ROS, PBUD, 사사키 가이드라인)의 발전 양상과 설계 전략의 패러다임 변화를 문헌 기반으로 조명합니다.
- **대표 소스 (Top 3~5)**:
  - **"도시공원 및 도시녹지 연구의 패러다임 변천과 사사키(Sasaki) 및 NRPA 가이드라인 기반의 통합적 관리 체계..."**: 시카고 학파의 고전적 도시 생태학에서 출발해 현대의 '사회-생태-기술 시스템(SETS)'으로 전환되는 담론과 사사키(Sasaki)의 친환경 관리 가이드라인의 접점을 서지학적으로 맵핑함 [15, 16].
  - **"Theoretical studies and design models of High Line parks: a systematic review"**: 폐기된 인프라를 활용한 선형 공원인 '하이라인 파크' 모델과 관련된 다학제적 연구 주제와 4가지 설계 원형(Design model)을 범주화함 [17, 18].
  - **"An Analytical Approach to Urban Landscape Planning Studies: Bibliometric Analysis"**: 조경 계획 접근법이 경관, 관리, 토지 이용, 생태계 서비스 중심으로 21년간 발전해 온 흐름을 R 프로그램과 WOS 데이터를 이용해 도출함 [19, 20].
- **기타 주요 소속 소스**: 
  - Bibliometric and Systematic Analysis of the Evolving Paradigms in Urban Park Management [21]
  - Bibliometric Trajectories and Socio-Ecological Resilience Frameworks in Urban Park Management [22]

### 군집 E: 거시적 핫스팟 및 30년 진화 궤적 (Macro 30-year Trends & Hotspots) (약 3개)
- **공통된 뼈대/서사**: 특정 세부 주제에 국한되지 않고, 지난 20~30년간 도시 공원 연구 전체의 국가별 주도권 변화(북미/서유럽 → 아시아/중국 등)와 주요 핫스팟의 폭넓은 변천사를 보여주는 매크로 리뷰 논문들입니다.
- **대표 소스 (Top 3~5)**:
  - **"A systematic review of urban green space research over the last 30 years: A bibliometric analysis"**: 지난 30년 동안 UGS 연구가 어떻게 산림 생태학에서 환경 정의 및 접근성 등 사회적 측면으로 이동했는지, 중심지가 서구에서 중국/EU 등으로 이동했는지 보여줌 [23, 24].
  - **"Advances, hotspots, and trends in restorative environment research over the past 30 years"**: 1993년부터 2024년까지의 '회복 환경(Restorative environment)' 연구의 확장을 다루며, 코로나19 팬데믹을 거치며 학술적 관심이 폭발적으로 증가했음을 시사함 [25].
  - **"Urban Green Space Research Progress and Hotspots Evolution Analysis"**: 생물 다양성, 열 환경, 녹지 접근성 등으로 진화하는 연구 핫스팟과 학제 간 융합을 조명함 [26, 27].

---

## 3. 주변부 소스 (Peripheral Sources) 💡
*주요 서지학 리뷰 군집에 명확히 들어맞지는 않지만, 서지학적 마이닝 기법과 실행 단계를 연결하는 흥미로운 특이점(세렌디피티)을 제공하는 소스입니다.*
- **"A new framework for assessment of park management in smart cities: a study based on social media data and deep learning"**: 이 문헌은 과거의 문헌을 리뷰하는 전형적인 '서지학 연구'라기보다는, 서지학에서 자주 쓰이는 '텍스트 마이닝 및 감성 분석' 기법(딥러닝)을 실제 스마트 시티의 '공원 실시간 관리 평가 프레임워크'로 직접 구현한 기술적 적용 사례로, 리뷰(Review)에서 실천(Practice)으로 넘어가는 징검다리 역할을 합니다 [28, 29].

## 4. AI의 대안적 분류 제안 (Facilitator's Recommendation)
*현재 적용된 '세부 연구 타겟' 기준 외에, 다음과 같은 기준으로 문헌을 다시 묶어보시면 서지학 문헌 안에서 새로운 통찰을 얻으실 수 있습니다.*
- **추천 기준 1: 분석 도구 및 데이터 소스 단위 (예: VOSviewer 중심 vs CiteSpace 중심 vs 빅데이터/소셜미디어 마이닝 기반)** 
  (이유: 서지학 연구가 어떤 툴과 데이터 소스(논문 메타데이터 vs 일반 시민의 트위터/리뷰 데이터)를 사용했느냐에 따라 도출할 수 있는 통찰의 결이 다릅니다. '데이터 관점'으로 군집을 나누면, 향후 연구자가 직접 리뷰 논문을 작성할 때 적합한 방법론을 선택하는 데 큰 도움이 됩니다.)
- **추천 기준 2: 문헌이 포괄하는 시간적 스케일 (예: 2000년 이전부터의 30년 초장기 리뷰 vs 최근 10년간의 급격한 패러다임 리뷰)**
  (이유: 30년 이상의 궤적을 살핀 문헌들은 도시 생태학이나 조경학의 근본적인 역사적 변천(Top-down)을 보여주는 반면, 2010년대 이후 단기 문헌들을 살핀 연구들은 AI, 스마트시티, 코로나19 등의 특정 사회 기술적 충격에 학계가 어떻게 단기적으로 반응했는지(Bottom-up)를 보여줍니다. 시계열적 렌즈로 분류하면 연구 동력의 차이를 읽어낼 수 있습니다.)
