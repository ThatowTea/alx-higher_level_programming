#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to first node in the list
 * Return: pointer to first node in the new list
 **/
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *now = *head;
	listint_t *next = NULL;

	while (now)
	{
		next = now->next;
		now->next = prev;
		prev = now;
		now = next;
	}

	*head = prev;
}

/**
 * is_palindrome - palindrome List
 * @head: double pointer to linked list
 * Return: 1 for expected result
 **/
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			dup = slow->next;
			break;
		}
		if (!fast->next)
		{
			dup = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_listint(&dup);

	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
}
