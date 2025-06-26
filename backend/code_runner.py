import io
import contextlib
import pandas as pd
import matplotlib.pyplot as plt
import base64

def execute_user_code(code, df):
    output = io.StringIO()
    img_buf = io.BytesIO()
    exec_globals = {"df": df, "pd": pd, "plt": plt}

    with contextlib.redirect_stdout(output):
        try:
            exec(code, exec_globals)
            if plt.get_fignums():
                plt.savefig(img_buf, format="png")
                plt.close()
                img_buf.seek(0)
                img_base64 = base64.b64encode(img_buf.read()).decode("utf-8")
                return {"text": output.getvalue(), "plot": img_base64}
            return {"text": output.getvalue()}
        except Exception as e:
            return {"error": str(e)}
