import streamlit as st
import json
import time

# ==========================================
# 1. 页面基本设置
# ==========================================
st.set_page_config(page_title="Elliott MedTerm AI Hub", page_icon="🩺", layout="wide")

# 侧边栏品牌露出
with st.sidebar:
    st.title("👨‍🏫 Elliott Cao")
    st.markdown("---")
    st.info("Medical Terminology Coaching\n\n*Scientia lumen vitae*")
    st.write("当前版本: v0.2 (Testing)")

# ==========================================
# 2. 数据加载
# ==========================================
@st.cache_data
def load_data():
    try:
        with open('mock_database.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

db = load_data()

# ==========================================
# 3. 主界面布局
# ==========================================
st.title("🩺 Elliott 医学英语交互式学习中心")

# 使用 Tabs 分割正向解析与反向生成
tab1, tab2 = st.tabs(["🧩 术语解剖室 (Deconstructor)", "🔨 术语铸造厂 (Forge)"])

# ------------------------------------------
# Tab 1: 术语解剖室逻辑
# ------------------------------------------
with tab1:
    st.subheader("医学术语结构化解析")
    
    # 分类快捷入口
    st.markdown("##### 🚀 快速开始 / 训练分类")
    cat_col1, cat_col2, cat_col3, cat_col4 = st.columns(4)
    
    selected_word = ""
    with cat_col1:
        if st.button("🅰️ 构词法极限挑战"):
            selected_word = "otorhinolaryngology"
    with cat_col2:
        if st.button("🅱️ 变态复数训练"):
            selected_word = "appendices"
    with cat_col3:
        if st.button("🫀 心血管系统专场"):
            selected_word = "pericarditis"
    with cat_col4:
        if st.button("🎲 随机词汇挑战"):
            import random
            selected_word = random.choice(list(db.keys())) if db else ""

    # 输入框
    user_input = st.text_input("👇 请在此输入或粘贴医学单词:", value=selected_word)

    if st.button("开始解析", key="decon_btn"):
        if user_input.lower() in db:
            data = db[user_input.lower()]
            with st.spinner("正在进行结构化解剖..."):
                time.sleep(1)
                st.success(f"解析成功: **{user_input.upper()}**")
                
                # UI 卡片展示 (Chapter 1)
                st.markdown("### 🧩 Chapter 1: Basic Word Structure")
                comps = data['chapter1_structure']['components']
                cols = st.columns(len(comps))
                for idx, c in enumerate(comps):
                    with cols[idx]:
                        st.info(f"**{c['part']}**\n\n*{c['type']}*\n\n{c['meaning']}")
                st.caption(f"🧬 Combining Form: {data['chapter1_structure']['combining_form']} | 📖 Rule: {data['chapter1_structure']['rule_applied']}")
                
                st.divider()
                
                # 扩展规则展示 (Chapter 2)
                st.markdown("### 🔄 Chapter 2: Pronunciation & Plurals")
                c1, c2 = st.columns(2)
                with c1:
                    st.write(f"🗣️ **发音规则:** {data['chapter2_extensions']['pronunciation_rule']}")
                    st.write(f"🧠 **记忆秘诀:** {data['chapter2_extensions']['mnemonics_eponyms']}")
                with c2:
                    st.write(f"📚 **复数形式:** `{data['chapter2_extensions']['plural_form']}`")
                    st.write(f"📖 **推演逻辑:** {data['chapter2_extensions']['plural_rule_explanation']}")
        else:
            st.warning("MVP 测试版：目前数据库仅包含选定的测试词汇。接入 AI 后即可解析全库。")

# ------------------------------------------
# Tab 2: 术语铸造厂逻辑 (反向生成)
# ------------------------------------------
with tab2:
    st.subheader("🔬 术语自定义铸造单元 (Custom Forge)")
    st.markdown("根据你的科研需求或解剖学描述，由 AI 指导合成正确的医学拼写。")
    
    desc_input = st.text_area("✍️ 请输入你想表达的医学含义 (例如: Surgical removal of the gallbladder):", 
                              placeholder="例如: Inflammation around the heart...")
    
    if st.button("开始铸造 (Forge Term)"):
        with st.spinner("AI 正在检索底层词根库并应用拼写规则..."):
            time.sleep(1.5)
            # 模拟反向生成的逻辑
            if "gallbladder" in desc_input.lower() and "removal" in desc_input.lower():
                st.markdown("### 🛠️ 铸造报告 (Diagnostic Report)")
                st.success("建议拼写: **Cholecystectomy**")
                
                st.markdown("#### ⚙️ 合成方案")
                st.code("""
1. 提取词根: Chole (胆汁) + Cyst (囊/胆囊)
2. 提取后缀: -ectomy (切除术)
3. 拼写校准: 根据 Vowel Drop Rule，Cyst 结尾为辅音，后缀 ectomy 开头为元音，
   省略中间的连接元音 o。
                """, language="markdown")
                
                st.warning("💡 **科研提醒:** 在正式论文中使用此术语时，请确保符合最新的 ICD-11 命名规范。")
            else:
                st.info("此功能目前为 UI 演示版。正式版接入 AI 大脑后，将支持任意复杂含义的术语合成。")

# ==========================================
# 4. 商业引导区
# ==========================================
st.write("---")
st.markdown("""
<div style='background-color: #f8f9fa; padding: 25px; border-radius: 12px; border-left: 6px solid #ff4b4b;'>
    <h3>🎓 进阶之路：医学拉丁文语法课</h3>
    <p>工具只能帮你查词，而思维能让你创造词。掌握底层拉丁文音素与变格规则，才是医学生的最高专业护城河。</p>
    <a href='#' style='color: #ff4b4b; font-weight: bold; text-decoration: none;'>👉 点击报名：Elliott 基础医学术语与拉丁文核心班</a>
</div>
""", unsafe_allow_html=True)
