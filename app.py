import streamlit as st
import json
import time

# ==========================================
# 1. 网页基本设置 & 品牌信息
# ==========================================
st.set_page_config(page_title="Elliott MedTerm AI", page_icon="🩺", layout="wide")

st.title("🩺 Elliott MedTerm AI")
st.subheader("医学英语词汇：基于大纲的智能结构化拆解")
st.markdown("基于 *Fundamentals of Medical Terminology* (Course 1003EMC) 核心逻辑构建。")

# ==========================================
# 2. 读取本地数据库文件
# ==========================================
@st.cache_data # 使用 Streamlit 缓存机制，加快读取速度
def load_mock_data():
    with open('mock_database.json', 'r', encoding='utf-8') as f:
        return json.load(f)

MOCK_DATABASE = load_mock_data()

# ==========================================
# 3. 页面主交互区
# ==========================================
st.write("---")
st.markdown("💡 **Demo 测试词汇推荐**: `pericarditis`, `gastroenterology`, `erythrocyte`, `appendix`")
user_input = st.text_input("👇 请输入一个医学英语单词:")

if st.button("🚀 AI 智能解析 (Deconstruct)"):
    word_key = user_input.strip().lower()
    
    if not word_key:
        st.warning("请输入单词后再解析。")
    else:
        # 模拟 AI 思考的延迟感
        with st.spinner("🤖 Elliott AI 正在调用大脑进行硬核拆解，请稍候..."):
            time.sleep(1.2) 
            
            if word_key in MOCK_DATABASE:
                data = MOCK_DATABASE[word_key]
                st.success(f"解析成功: **{data['term'].upper()}**")
                
                # --- 第一章 构词法 UI ---
                st.markdown("### 🧩 第一章：构词法拆解 (Basic Word Structure)")
                components = data['chapter1_structure']['components']
                
                cols = st.columns(len(components))
                for i, comp in enumerate(components):
                    with cols[i]:
                        if comp['type'] == "Word Root":
                            st.info(f"**{comp['part']}**\n\n*{comp['type']}*\n\n{comp['meaning']}")
                        elif comp['type'] == "Combining Vowel":
                            st.warning(f"**{comp['part']}**\n\n*{comp['type']}*\n\n{comp['meaning']}")
                        elif comp['type'] == "Prefix":
                            st.success(f"**{comp['part']}**\n\n*{comp['type']}*\n\n{comp['meaning']}")
                        else: # Suffix
                            st.error(f"**{comp['part']}**\n\n*{comp['type']}*\n\n{comp['meaning']}")
                
                st.write(f"🧬 **组合形式 (Combining Form):** `{data['chapter1_structure']['combining_form']}`")
                st.write(f"📖 **拼读法则分析:** {data['chapter1_structure']['rule_applied']}")
                st.divider()
                
                # --- 第二章 扩展规则 UI ---
                st.markdown("### 🔄 第二章：发音、复数与记忆术 (Extensions)")
                ext = data['chapter2_extensions']
                col_a, col_b = st.columns(2)
                
                with col_a:
                    st.markdown("#### 🗣️ 发音规则 (Pronunciation)")
                    st.write(ext['pronunciation_rule'])
                    st.markdown("#### 🧠 记忆术/命名法 (Mnemonics & Eponyms)")
                    st.write(ext['mnemonics_eponyms'])
                with col_b:
                    st.markdown("#### 📚 单复数推演 (Plurals)")
                    st.write(f"**复数形式:** `{ext['plural_form']}`")
                    st.write(f"**推演规则:** {ext['plural_rule_explanation']}")

            else:
                st.info(f"⚠️ 这是一个 MVP 演示版。目前本地数据库未包含此词汇。\n\n正式版接入 API 大脑后，即可解析您输入的 `{user_input}`！")

# ==========================================
# 4. 商业闭环（引流区）
# ==========================================
st.write("---")
st.markdown("""
<div style='background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid #ff4b4b;'>
    <h4>💡 想要系统性建立医学词汇直觉？</h4>
    <p>AI 工具只是辅助！医学英语中 80% 的词汇来源于拉丁语和希腊语。掌握底层的发音法则与核心词根，才能真正做到“见词拆意”。</p>
    <a href='#' style='text-decoration: none; font-weight: bold; color: #ff4b4b;'>👉 点击试看：Elliott 基础医学术语及拉丁文语法速成班</a>
</div>
""", unsafe_allow_html=True)
