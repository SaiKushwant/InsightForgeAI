from workflow import app_graph

topic = input("Enter your research topic: ")

result = app_graph.invoke(
    {
        "topic": topic
    }
)

print("\n")
print("=" * 80)
print(result["report"])
print("=" * 80)