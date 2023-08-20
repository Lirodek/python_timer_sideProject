import java.util.*;
class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        int[] answer = new int[privacies.length];
        HashMap<String, Integer> termsMap = new HashMap<>();
        String todays[] = today.split("\\.");
        int cnt=0;
        today = today.replace(".", "");
        for(String temp : terms){
            String tempArr[] =temp.split(" ");
            termsMap.put( tempArr[0], Integer.parseInt(tempArr[1]) );
        }

        for(int i=0; i<privacies.length; i++){
            String tempToday = privacies[i].split(" ")[0];
            String conditionsType = privacies[i].split(" ")[1];
            String tempArr[] = tempToday.split("\\.");

            Integer targetMonth = termsMap.get(conditionsType) + Integer.parseInt( tempArr[1] );
            Integer targetDay = Integer.parseInt(tempArr[2]) -1 ;

            tempArr[1] = targetMonth<10 ? "0"+String.valueOf(targetMonth) : String.valueOf(targetMonth);
            tempArr[2] = targetDay < 10 ? "0" + String.valueOf(targetDay) : String.valueOf(targetDay);

            if(targetDay< 1){
                targetMonth -= 1;
                tempArr[1] = String.valueOf(targetMonth);
                targetDay = 28;
                tempArr[2] = targetDay < 10 ? "0" + String.valueOf(targetDay) : String.valueOf(targetDay);
            }
            if(targetMonth > 12 ){
                int excessYears = (targetMonth / 12);
               
                targetMonth = (targetMonth % 12) == 0 ? 1 : (targetMonth % 12);
                tempArr[0] = String.valueOf(Integer.parseInt( tempArr[0] )+excessYears);
                tempArr[1] = String.valueOf(targetMonth);
            }


            if(!(Integer.parseInt(tempArr[0]) <= Integer.parseInt(todays[0]))){
                continue;
            }else if(Integer.parseInt(tempArr[0]) == Integer.parseInt(todays[0])){
                if(!(Integer.parseInt(tempArr[1]) <= Integer.parseInt(todays[1]))){
                    continue;
                } else if(Integer.parseInt(tempArr[1]) == Integer.parseInt(todays[1])){
                    if(!(Integer.parseInt(tempArr[2]) < Integer.parseInt(todays[2]))){
                        continue;
                    }
                }
            }
            answer[cnt++] = i+1;

        }
        int result[] = new int[cnt];
        for(int i=0; i<cnt;i++){
            result[i] = answer[i];
        }



        return result;
    }
}