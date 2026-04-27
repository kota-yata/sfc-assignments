#nullable enable
using GameCanvas;
using Unity.Mathematics;
using UnityEngine;
using UnityEngine.InputSystem;

/// <summary>
/// ゲームクラス。
/// 学生が編集すべきソースコードです。
/// </summary>
public sealed class Game : GameBase
{
    int money;
    const int CARD_TYPE = 10;
    int[] card_count = new int [CARD_TYPE];
    string[] card_name = {"A","B","C","D","E","F","G","H","I","J"};
    bool isComplete;
    int new_card ;

    /// <summary>
    /// 初期化処理
    /// </summary>
    public override void InitGame()
    {
        gc.ChangeCanvasSize(720, 1280);
        ResetGame();
    }

    public void ResetGame()
    {
        gc.SetRandomSeed((uint)gc.CurrentTimestamp*1024);
	    money = 10000;
	    for (int i = 0; i < CARD_TYPE; i++) {
	    	card_count[i] = 0;
	    }
	    isComplete = false;
	    new_card = -1;
    }

    public int GetNewCard()
    {
        new_card = gc.Random(5, 9);
        int probability = gc.Random(0, 3);
        if (probability == 0)
        {
            new_card = gc.Random(0, 4);
        }
        return new_card;
    }

    /// <summary>
    /// 動きなどの更新処理
    /// </summary>
    public override void UpdateGame()
    {
        if (gc.GetPointerFrameCount(0) >= 120) {
            ResetGame();
        } else if (gc.GetPointerFrameCount(0)==1 && ! isComplete) {
            money -= 100;
            new_card = GetNewCard();
            card_count[new_card]++;

            if (new_card <= 4 && card_count[new_card] >= 5) {
                isComplete = true;
            }
        }
    }

    /// <summary>
    /// 描画の処理
    /// </summary>
    public override void DrawGame()
    {
        gc.ClearScreen();
        gc.SetColor(0,0,0);
        gc.SetFontSize(36);
        gc.DrawString("money:"+money,60, 40);

        if(new_card >= 0){
        gc.DrawString("new:"+card_name[new_card],60, 80);
        }

        for(int i=0 ; i< CARD_TYPE ; i++){
            gc.DrawString(card_name[i] + ":" + card_count[i],60, 120+i*40);
        }

        if(isComplete ){
        gc.DrawString("complete!!",60, 520);
        }
    }
}
