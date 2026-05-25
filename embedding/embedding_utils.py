def embed_texts(embeddings, texts):
    try:
        texts = [t for t in texts if isinstance(t, str) and t.strip()]

        if not texts:
            raise ValueError("No valid input texts provided")

        result = []

        for text in texts:
            vec = embeddings.embed_query(text)

            if not vec:
                raise ValueError(f"No embedding for text: {text}")

            result.append(vec)

        return result

    except Exception as e:
        raise Exception(f"Error generating embeddings: {str(e)}")


def embed_query(embeddings, query):
    """
    Convert user query into embedding
    """
    try:
        # ✅ Validate query
        if not query or not query.strip():
            raise ValueError("Empty query provided")

        # ✅ Generate embedding
        result = embeddings.embed_query(query)

        # ✅ Validation
        if not result:
            raise ValueError("No embedding data received for query")

        if not isinstance(result, (list, tuple)):
            raise ValueError("Invalid query embedding format")

        return result

    except Exception as e:
        raise Exception(f"Error embedding query: {str(e)}")
