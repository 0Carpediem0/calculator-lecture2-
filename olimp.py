def check_winners(scores: list, student_score: int) -> None:
    sorted_scores = sorted(scores, reverse=True)
    top3 = sorted_scores[:3]
    if student_score in top3:
        print("Вы в тройке победителей!")
    else:
        print("Вы не попали в тройку победителей.")
