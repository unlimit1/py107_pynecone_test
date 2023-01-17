import pynecone as pc


config = pc.Config(
    app_name="py107_pynecone_test",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
