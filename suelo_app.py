import streamlit as st

st.set_page_config(page_title="Calculadora de Mecánica de Suelos", layout="centered")

st.title("📘 Calculadora de Relaciones de Suelos")

st.sidebar.header("Módulos")
modulo = st.sidebar.selectbox(
    "Selecciona el módulo",
    [
        "Relaciones de peso",
        "Relación de vacíos (e)",
        "Porosidad (n)",
        "Peso unitario total (γ)",
        "Peso unitario seco (γd)"
    ]
)

# -----------------------------
# RELACIONES DE PESO
# -----------------------------
if modulo == "Relaciones de peso":
    st.header("Relaciones de peso")

    opcion = st.selectbox("¿Qué deseas calcular?", ["WT", "Ws", "Ww"])

    if opcion == "WT":
        Ws = st.number_input("Peso de sólidos (Ws)", min_value=0.0)
        Ww = st.number_input("Peso de agua (Ww)", min_value=0.0)

        if st.button("Calcular WT"):
            WT = Ws + Ww
            st.success(f"WT = {WT:.4f}")

    elif opcion == "Ws":
        WT = st.number_input("Peso total (WT)", min_value=0.0)
        Ww = st.number_input("Peso de agua (Ww)", min_value=0.0)

        if st.button("Calcular Ws"):
            Ws = WT - Ww
            st.success(f"Ws = {Ws:.4f}")

    elif opcion == "Ww":
        WT = st.number_input("Peso total (WT)", min_value=0.0)
        Ws = st.number_input("Peso de sólidos (Ws)", min_value=0.0)

        if st.button("Calcular Ww"):
            Ww = WT - Ws
            st.success(f"Ww = {Ww:.4f}")

# -----------------------------
# RELACIÓN DE VACÍOS
# -----------------------------
elif modulo == "Relación de vacíos (e)":
    st.header("Relación de vacíos")

    opcion = st.selectbox("¿Qué deseas calcular?", ["e", "Vv", "Vs"])

    if opcion == "e":
        Vv = st.number_input("Volumen de vacíos (Vv)", min_value=0.0)
        Vs = st.number_input("Volumen de sólidos (Vs)", min_value=0.0)

        if st.button("Calcular e"):
            if Vs != 0:
                e = Vv / Vs
                st.success(f"e = {e:.4f}")
            else:
                st.error("Vs no puede ser cero")

    elif opcion == "Vv":
        e = st.number_input("Relación de vacíos (e)", min_value=0.0)
        Vs = st.number_input("Volumen de sólidos (Vs)", min_value=0.0)

        if st.button("Calcular Vv"):
            Vv = e * Vs
            st.success(f"Vv = {Vv:.4f}")

    elif opcion == "Vs":
        Vv = st.number_input("Volumen de vacíos (Vv)", min_value=0.0)
        e = st.number_input("Relación de vacíos (e)", min_value=0.0)

        if st.button("Calcular Vs"):
            if e != 0:
                Vs = Vv / e
                st.success(f"Vs = {Vs:.4f}")
            else:
                st.error("e no puede ser cero")

# -----------------------------
# POROSIDAD
# -----------------------------
elif modulo == "Porosidad (n)":
    st.header("Porosidad")

    opcion = st.selectbox("¿Qué deseas calcular?", ["n", "Vv", "VT"])

    if opcion == "n":
        Vv = st.number_input("Volumen de vacíos (Vv)", min_value=0.0)
        VT = st.number_input("Volumen total (VT)", min_value=0.0)

        if st.button("Calcular n"):
            if VT != 0:
                n = Vv / VT
                st.success(f"n = {n:.4f}")
            else:
                st.error("VT no puede ser cero")

# -----------------------------
# PESO UNITARIO TOTAL
# -----------------------------
elif modulo == "Peso unitario total (γ)":
    st.header("Peso unitario total")

    WT = st.number_input("Peso total (WT)", min_value=0.0)
    VT = st.number_input("Volumen total (VT)", min_value=0.0)

    if st.button("Calcular γ"):
        if VT != 0:
            gamma = WT / VT
            st.success(f"γ = {gamma:.4f}")
        else:
            st.error("VT no puede ser cero")

# -----------------------------
# PESO UNITARIO SECO
# -----------------------------
elif modulo == "Peso unitario seco (γd)":
    st.header("Peso unitario seco")

    Ws = st.number_input("Peso de sólidos (Ws)", min_value=0.0)
    VT = st.number_input("Volumen total (VT)", min_value=0.0)

    if st.button("Calcular γd"):
        if VT != 0:
            gamma_d = Ws / VT
            st.success(f"γd = {gamma_d:.4f}")
        else:
            st.error("VT no puede ser cero")
