#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 * Return: 0 if no cycle, 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list;
	fast = list->next;

	while (slow != fast)
	{
		if (fast == NULL || fast->next == NULL)
			return (0);

		slow = slow->next;
		fast = fast->next->next;
	}
	return (1);
}
